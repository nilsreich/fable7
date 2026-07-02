// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import { unified } from '@astrojs/markdown-remark';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

// https://astro.build/config
export default defineConfig({
	markdown: {
		processor: unified({
			remarkPlugins: [remarkMath],
			rehypePlugins: [rehypeKatex],
		}),
	},
	integrations: [
		starlight({
			title: 'Mathe BGY 11',
			description:
				'Mathematik für die Jahrgangsstufe 11 des Beruflichen Gymnasiums – Erklärungen, Beispiele und Übungsaufgaben mit Lösungen.',
			locales: {
				root: { label: 'Deutsch', lang: 'de' },
			},
			head: [
				{
					// Beamer-Modus: ?beamer aktiviert, ?beamer=off deaktiviert.
					// Der Zustand überlebt Seitenwechsel per sessionStorage.
					tag: 'script',
					content: `(function () {
  var s = location.search;
  if (s.indexOf('beamer=off') > -1) sessionStorage.removeItem('beamer');
  else if (s.indexOf('beamer') > -1) sessionStorage.setItem('beamer', '1');
  if (sessionStorage.getItem('beamer')) document.documentElement.classList.add('beamer');
})();`,
				},
			],
			customCss: ['katex/dist/katex.min.css', './src/styles/custom.css'],
			sidebar: [
				{ label: 'Basiswissen', items: [{ autogenerate: { directory: 'basiswissen' } }] },
				{ label: 'Funktionen', items: [{ autogenerate: { directory: 'funktionen' } }] },
				{
					label: 'Ganzrationale Funktionen',
					items: [{ autogenerate: { directory: 'ganzrationale' } }],
				},
				{
					label: 'Differentialrechnung',
					items: [{ autogenerate: { directory: 'differentialrechnung' } }],
				},
				{
					label: 'Kurvendiskussion',
					items: [{ autogenerate: { directory: 'kurvendiskussion' } }],
				},
				{
					label: 'Kurvenscharen & Ortskurven',
					items: [{ autogenerate: { directory: 'scharen' } }],
				},
				{
					label: 'Extremwertprobleme',
					items: [{ autogenerate: { directory: 'extremwertprobleme' } }],
				},
				{
					label: 'Steckbriefaufgaben & LGS',
					items: [{ autogenerate: { directory: 'steckbriefaufgaben' } }],
				},
			],
		}),
	],
});
