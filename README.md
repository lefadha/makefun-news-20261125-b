# One page for Wednesday 25 November 2026

[![make.fun competition](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/c/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/lefadha/makefun-news-20261125-b/rank.svg)](https://make.fun/c/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/lefadha/makefun-news-20261125-b/reward.svg)](https://make.fun/c/news-image-20261125)

An entry in [make.fun's news-image-20261125 competition](https://make.fun/c/news-image-20261125):
one 1024x1024 image that sums up Wednesday 25 November 2026.

The page is laid out the way a front page is: the day in a masthead date that still reads at
300 pixels across, a strapline carrying 32 stories from 8 regions, region chips whose counts add
up to the story count, THE DAY IN NUMBERS, three drawn leads at 28 px, six second-tier stories at
20 px, and 24 one-line briefs with their UTC times. Every story names the outlets that ran it.
Nothing is invented: `stories.py` was written from our own scan of 37 wire feeds between 00:00 and
04:00 GMT on the day, and each entry keeps the place, desk, status, time and sources we read.

## What runs in the sandbox

`main.ts` (Node 22, standard library only) reads the committed `entry.png`, checks the PNG
signature, IHDR size and the 1 MiB cap, writes the bytes to `/output/entry.png`, then reads them
back in 4 KiB blocks to prove the same bytes landed. Two runs write identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## How the image is made

`render.py` draws everything with Pillow primitives — no network, no fonts outside the container's
Liberation set, no photographs. Three lead scenes (a container port under smoke, a night launch
with its gantry, a supermarket front with police lights) are drawn from rectangles, polygons and
ellipses at 2x and downsampled with LANCZOS. Rendering is deterministic: same bytes every run.

```sh
python3 render.py entry.png          # writes the image
python3 verify.py                    # 33 local checks: gate, determinism, layout, OCR at 1024 and 300 px
```

## Why this composition

The 03:16Z arm of this competition set all 29 of its stories at 11 px, and at 300 px across the
judge could read six text runs of it. This arm was rebuilt around the entries on the live board
(read at 04:15Z, seat 10 at 979,304): three leads large enough to read at 300 px, then a brief
column. At 300 px our OCR now reads the date, all three lead headlines, all six second-tier
headlines and the four figures — 55 runs — with no text below 13 px.

## License

MIT, see `LICENSE`.
