// Interaktive Ergänzungen ohne Framework – bewusst klein gehalten.
//
// 1. Checklisten zur Klassenarbeit: Die aus Markdown ("- [ ]") erzeugten
//    Kästchen sind standardmäßig deaktiviert. Hier werden sie freigeschaltet
//    und der Stand pro Seite in localStorage gemerkt, damit die
//    Selbsteinschätzung beim nächsten Besuch noch da ist.
// 2. Beamer-Schalter: kleiner Knopf unten rechts, der den Beamer-Modus
//    ohne URL-Parameter umschaltet (gleicher sessionStorage-Zustand wie
//    das ?beamer-Skript im <head>).
// 3. Laserpointer: Im Beamer-Modus ersetzt ein roter Leuchtpunkt den
//    Cursor und folgt Maus, Stift und Finger (Sichtbarkeit regelt CSS).
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

		// --- Beamer-Schalter --------------------------------------------------
		var knopf = document.createElement('button');
		knopf.type = 'button';
		knopf.className = 'beamer-schalter';
		function beschrifte() {
			var an = document.documentElement.classList.contains('beamer');
			knopf.textContent = an ? 'Beamer aus' : 'Beamer';
			knopf.setAttribute('aria-pressed', an ? 'true' : 'false');
		}
		knopf.addEventListener('click', function () {
			var html = document.documentElement;
			html.classList.toggle('beamer');
			if (html.classList.contains('beamer')) sessionStorage.setItem('beamer', '1');
			else sessionStorage.removeItem('beamer');
			beschrifte();
		});
		beschrifte();
		document.body.appendChild(knopf);

		// --- Laserpointer -----------------------------------------------------
		var laser = document.createElement('div');
		laser.className = 'laserpunkt';
		laser.setAttribute('aria-hidden', 'true');
		laser.style.transform = 'translate(-100px, -100px)'; // bis zur ersten Bewegung außerhalb
		document.body.appendChild(laser);
		function zeige(e) {
			laser.style.transform = 'translate(' + e.clientX + 'px, ' + e.clientY + 'px)';
		}
		document.addEventListener('pointermove', zeige, { passive: true });
		document.addEventListener('pointerdown', zeige, { passive: true });

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
