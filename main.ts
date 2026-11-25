// The entry: one page for Wednesday 25 November 2026, drawn by render.py and
// committed as entry.png. This program copies those exact bytes to the output
// directory, then reads them back and re-checks the gate's own limits before
// exiting, so a run that would be refused can never look like it succeeded.
//
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const MAX_BYTES = 1048576;
const SOURCE = new URL('./entry.png', import.meta.url);
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });

const bytes = readFileSync(SOURCE);
if (bytes.length > MAX_BYTES) throw new Error(`entry.png is ${bytes.length} bytes, over the 1 MiB cap`);
const sig = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a];
for (let i = 0; i < sig.length; i++) {
  if (bytes[i] !== sig[i]) throw new Error('entry.png is not a PNG');
}
const width = bytes.readUInt32BE(16);
const height = bytes.readUInt32BE(20);
if (width !== 1024 || height !== 1024) throw new Error(`entry.png is ${width}x${height}, not 1024x1024`);

const target = join(outDir, 'entry.png');
writeFileSync(target, bytes);
const back = readFileSync(target);
if (back.length !== bytes.length) throw new Error('the written file is not the same length');
for (let i = 0; i < bytes.length; i += 4096) {
  const end = Math.min(i + 4096, bytes.length);
  if (!back.subarray(i, end).equals(bytes.subarray(i, end))) throw new Error('the written file differs');
}
console.log(`wrote ${target}: ${bytes.length} bytes, ${width}x${height}`);
