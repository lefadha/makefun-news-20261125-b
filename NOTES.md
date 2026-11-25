# Build notes — arm 2 of news-image-20261125 (25 Nov 2026, 04:1x-04:4x Z)

## What was measured before this arm was drawn

The competition runs live development heats, so the board is public while the contest is open.
Read at 04:15Z: 400 rows, seat 10 = 979,304, leader = 986,426 (213,394 B), field 3,080 entries of
which 337 were graded. Our own 03:16Z arm was not among them — the dev queue had not reached it —
so this arm could not be measured against our own rate. It was designed against the board instead.

The top three entries' artifacts were pulled and OCR'd with our own rapidocr at 1024 and at 300 px:

| rank | judge | bytes | light % | colour % | OCR runs at 1024 | at 300 px |
|---|---|---|---|---|---|---|
| 1 | 986,426 | 213,394 | 72.5 | 15.8 | 129 | 20 |
| 2 | 985,867 | 288,452 | 72.1 | 13.9 | 133 | 25 |
| 3 | 984,664 | 249,501 | 65.7 | 13.1 | 137 | 20 |
| 5 | 982,970 | 382,147 | 76.1 | 8.8 | 173 | 10 |
| ours (03:16Z arm) | — | 195,127 | 70.4 | 12.8 | 236 | 6 |

Two things fall out of the table. First, the paid band is NOT optimised for wide text: rank 1 keeps
only 20 readable runs at 300 px and rank 5 keeps 10, so "more text" is not the lever. Second, every
entry in the band has a small number of large headlines: the OCR of rank 1 reads its three lead
headlines whole at 300 px plus the date and four figures. Our arm had 236 text runs at full size and
six at 300 px — 29 stories all set at 11 px, which is mush at the size the judge reads.

## The one change in this arm

Structure and type size, nothing else: three leads with a drawn scene and a 28 px headline, six
second-tier stories at 20 px sans bold, 23 one-line briefs at 13.5 px, and the date set at 22 px so
it survives 300 px. Story count went 29 -> 32 (3 + 6 + 23), regions 8. Every line of text is at
13 px or larger; nothing is under it.

Measured after the change, same OCR method: 55 runs at 300 px, and at that size the date, all three
lead headlines, all six second-tier headlines, and the figures 74, 8.2m, 4.9%, 36% all read whole.
Full size reads 32/32 headlines and 23/23 briefs.

## What is deliberately not here

No photographs, no borrowed artwork, no text addressed to the judge. The three scenes are drawn from
Pillow primitives (rectangles, polygons, ellipses) at 2x and downsampled with LANCZOS, so the file is
our own work end to end and renders byte-identically on every run: the shipped file is 463,737 B,
sha256 524fcc572803…, and `verify.py` re-renders it twice and compares both against the committed
bytes on every run.
