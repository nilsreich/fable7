// Interaktive Ergänzungen ohne Framework – bewusst klein gehalten.
//
// 1. Checklisten zur Klassenarbeit: Die aus Markdown ("- [ ]") erzeugten
//    Kästchen sind standardmäßig deaktiviert. Hier werden sie freigeschaltet
//    und der Stand pro Seite in localStorage gemerkt, damit die
//    Selbsteinschätzung beim nächsten Besuch noch da ist.
// 2. Beamer-Schalter: kleiner Knopf unten rechts, der den Beamer-Modus
//    ohne URL-Parameter umschaltet (gleicher sessionStorage-Zustand wie
//    das ?beamer-Skript im <head>). Beim Einschalten wird das helle Theme
//    erzwungen (Projektoren!) und alle offenen Lösungen werden zugeklappt;
//    beim Ausschalten kommt das vorherige Theme zurück.
// 3. Übungs-Timer (nur im Beamer-Modus sichtbar): sichtbarer Countdown
//    für die Arbeitsrunden, überlebt Seitenwechsel per sessionStorage.
// 4. Service Worker für die PWA (Offline-Nutzung besuchter Seiten).
(function () {
	function init() {
		// --- Checklisten freischalten und Stand merken -----------------------
		var boxen = document.querySelectorAll(
			'.sl-markdown-content li.task-list-item > input[type="checkbox"]'
		);
		var schluessel = 'checkliste:' + location.pathname;
		var gemerkt = [];
		try {
			gemerkt = JSON.parse(localStorage.getItem(schluessel) || '[]');
		} catch (e) {
			/* defekter Eintrag → leer starten */
		}
		boxen.forEach(function (box, i) {
			box.disabled = false;
			box.checked = gemerkt.indexOf(i) > -1;
			box.addEventListener('change', function () {
				var stand = [];
				boxen.forEach(function (b, j) {
					if (b.checked) stand.push(j);
				});
				try {
					localStorage.setItem(schluessel, JSON.stringify(stand));
				} catch (e) {
					/* privater Modus o. Ä. → Häkchen gelten nur für diese Sitzung */
				}
			});
		});

		// --- Theme-Steuerung (nutzt Starlights eigenen Speicher) -------------
		function themeSetzen(wert) {
			// wert: 'light' | 'dark' | 'auto'
			var sichtbar =
				wert === 'auto'
					? matchMedia('(prefers-color-scheme: light)').matches
						? 'light'
						: 'dark'
					: wert;
			document.documentElement.dataset.theme = sichtbar;
			try {
				localStorage.setItem('starlight-theme', wert === 'auto' ? '' : wert);
			} catch (e) {}
			if (window.StarlightThemeProvider && StarlightThemeProvider.updatePickers) {
				StarlightThemeProvider.updatePickers(wert);
			}
		}
		function gespeichertesTheme() {
			var wert = '';
			try {
				wert = localStorage.getItem('starlight-theme') || '';
			} catch (e) {}
			return wert === 'light' || wert === 'dark' ? wert : 'auto';
		}

		// --- Beamer-Modus an/aus ----------------------------------------------
		var THEME_VORHER = 'beamer-theme-vorher';

		function beamerAn() {
			document.documentElement.classList.add('beamer');
			sessionStorage.setItem('beamer', '1');
			// Vorheriges Theme merken (nur beim Übergang, nicht bei jedem Seitenwechsel)
			if (sessionStorage.getItem(THEME_VORHER) === null) {
				sessionStorage.setItem(THEME_VORHER, gespeichertesTheme());
			}
			themeSetzen('light');
			// Offene Lösungen zuklappen – nichts aus der Vorbereitung verraten
			document.querySelectorAll('.sl-markdown-content details[open]').forEach(function (d) {
				d.open = false;
			});
		}

		function beamerAus() {
			document.documentElement.classList.remove('beamer');
			sessionStorage.removeItem('beamer');
			var vorher = sessionStorage.getItem(THEME_VORHER);
			if (vorher !== null) {
				themeSetzen(vorher);
				sessionStorage.removeItem(THEME_VORHER);
			}
		}

		// Abgleich beim Laden: Der Modus kann auch per ?beamer/?beamer=off im
		// <head>-Skript gewechselt worden sein – Theme dann hier nachziehen.
		var beamerAktiv = document.documentElement.classList.contains('beamer');
		if (beamerAktiv && sessionStorage.getItem(THEME_VORHER) === null) beamerAn();
		if (!beamerAktiv && sessionStorage.getItem(THEME_VORHER) !== null) beamerAus();

		// --- Leiste unten rechts: Timer + Beamer-Schalter ---------------------
		var leiste = document.createElement('div');
		leiste.className = 'ecken-leiste';

		var knopf = document.createElement('button');
		knopf.type = 'button';
		knopf.className = 'pult-knopf beamer-schalter';
		function beschrifte() {
			var an = document.documentElement.classList.contains('beamer');
			knopf.textContent = an ? 'Beamer aus' : 'Beamer';
			knopf.setAttribute('aria-pressed', an ? 'true' : 'false');
		}
		knopf.addEventListener('click', function () {
			if (document.documentElement.classList.contains('beamer')) beamerAus();
			else beamerAn();
			beschrifte();
		});
		beschrifte();

		// --- Übungs-Timer -------------------------------------------------------
		var TIMER_ENDE = 'timer-ende';
		var anzeige = document.createElement('button');
		anzeige.type = 'button';
		anzeige.className = 'timer-anzeige';
		anzeige.title = 'Timer beenden';
		document.body.appendChild(anzeige);

		var vorwahl = document.createElement('span');
		vorwahl.className = 'timer-vorwahl';
		var timerKnopf = document.createElement('button');
		timerKnopf.type = 'button';
		timerKnopf.className = 'pult-knopf timer-knopf';
		timerKnopf.textContent = 'Timer';
		timerKnopf.setAttribute('aria-expanded', 'false');
		timerKnopf.addEventListener('click', function () {
			var offen = vorwahl.classList.toggle('offen');
			timerKnopf.setAttribute('aria-expanded', offen ? 'true' : 'false');
		});

		var tickId = null;
		function timerStoppen() {
			sessionStorage.removeItem(TIMER_ENDE);
			if (tickId) clearInterval(tickId);
			tickId = null;
			anzeige.classList.remove('laeuft', 'abgelaufen');
		}
		function tick() {
			var ende = Number(sessionStorage.getItem(TIMER_ENDE));
			if (!ende) return timerStoppen();
			var rest = Math.max(0, Math.round((ende - Date.now()) / 1000));
			var m = Math.floor(rest / 60);
			var s = String(rest % 60).padStart(2, '0');
			anzeige.textContent = m + ':' + s;
			anzeige.classList.add('laeuft');
			if (rest === 0) {
				anzeige.classList.add('abgelaufen');
				if (tickId) clearInterval(tickId);
				tickId = null;
			}
		}
		function timerStarten(minuten) {
			sessionStorage.setItem(TIMER_ENDE, String(Date.now() + minuten * 60000));
			anzeige.classList.remove('abgelaufen');
			tick();
			if (!tickId) tickId = setInterval(tick, 500);
		}
		[5, 10, 15, 25].forEach(function (minuten) {
			var b = document.createElement('button');
			b.type = 'button';
			b.className = 'pult-knopf';
			b.textContent = minuten + ' min';
			b.addEventListener('click', function () {
				timerStarten(minuten);
				vorwahl.classList.remove('offen');
				timerKnopf.setAttribute('aria-expanded', 'false');
			});
			vorwahl.appendChild(b);
		});
		anzeige.addEventListener('click', timerStoppen);
		// Laufenden (oder gerade abgelaufenen) Timer nach Seitenwechsel fortsetzen
		if (sessionStorage.getItem(TIMER_ENDE)) {
			tick();
			if (!anzeige.classList.contains('abgelaufen')) tickId = setInterval(tick, 500);
		}

		leiste.appendChild(vorwahl);
		leiste.appendChild(timerKnopf);
		leiste.appendChild(knopf);
		document.body.appendChild(leiste);

		// --- Service Worker (PWA) ---------------------------------------------
		if ('serviceWorker' in navigator) {
			navigator.serviceWorker.register('/sw.js').catch(function () {
				/* z. B. lokal ohne HTTPS – die Seite funktioniert auch ohne */
			});
		}
	}

	if (document.readyState === 'loading') {
		document.addEventListener('DOMContentLoaded', init);
	} else {
		init();
	}
})();
