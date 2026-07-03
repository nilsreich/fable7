// Rastert scripts/pwa-icon.svg zu den PNG-Icons der PWA in public/.
// Aufruf: node scripts/pwa-icons.mjs  (sharp ist bereits Projektabhängigkeit)
import sharp from 'sharp';
import { fileURLToPath } from 'node:url';

const quelle = fileURLToPath(new URL('./pwa-icon.svg', import.meta.url));
const ziel = (name) => fileURLToPath(new URL(`../public/${name}`, import.meta.url));

const ausgaben = [
	['icon-192.png', 192],
	['icon-512.png', 512],
	['apple-touch-icon.png', 180],
];

for (const [name, groesse] of ausgaben) {
	await sharp(quelle, { density: 300 }).resize(groesse, groesse).png().toFile(ziel(name));
	console.log(`public/${name} (${groesse}×${groesse})`);
}
