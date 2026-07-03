// Service Worker der PWA: „stale-while-revalidate“ für alle GET-Anfragen
// der eigenen Herkunft. Jede besuchte Seite (samt Formeln, Plots, Stilen)
// landet im Cache und ist danach offline verfügbar; bei bestehender
// Verbindung wird der Cache im Hintergrund aktualisiert — Änderungen an
// den Inhalten erscheinen also spätestens beim übernächsten Aufruf.
var CACHE = 'mathe-bgy11-v1';

self.addEventListener('install', function () {
	self.skipWaiting();
});

self.addEventListener('activate', function (ereignis) {
	ereignis.waitUntil(
		caches
			.keys()
			.then(function (namen) {
				return Promise.all(
					namen
						.filter(function (name) {
							return name !== CACHE;
						})
						.map(function (name) {
							return caches.delete(name);
						})
				);
			})
			.then(function () {
				return self.clients.claim();
			})
	);
});

self.addEventListener('fetch', function (ereignis) {
	var anfrage = ereignis.request;
	if (anfrage.method !== 'GET') return;
	if (new URL(anfrage.url).origin !== self.location.origin) return;

	ereignis.respondWith(
		caches.open(CACHE).then(function (cache) {
			return cache.match(anfrage).then(function (gecacht) {
				var vomNetz = fetch(anfrage)
					.then(function (antwort) {
						if (antwort && antwort.ok) cache.put(anfrage, antwort.clone());
						return antwort;
					})
					.catch(function () {
						return gecacht;
					});
				return gecacht || vomNetz;
			});
		})
	);
});
