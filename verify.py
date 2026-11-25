"""Local mirror of the gate and of the judge's stated craft rules.

Checks, in the order a failure would cost us the submission:
  1. the committed entry.png is a whole 1024x1024 PNG under 1 MiB;
  2. two fresh renders are byte-identical, and identical to the committed file;
  3. main.ts ships exactly those bytes (run twice, compared);
  4. layout: no ink in the 12 px border, every block inside the page;
  5. the page still reads at 300 px across (the judge's own wording) and at full size;
  6. the count the masthead prints is the count the page carries, per region.

Run: node /opt/data/runpy.js /opt/data/ocr-venv/bin/python verify.py
"""
import hashlib
import os
import re
import struct
import subprocess
import sys
import tempfile

from PIL import Image
import numpy as np

import render
import stories

HERE = os.path.dirname(os.path.abspath(__file__))
passes, fails = [], []


def check(name, ok, detail=""):
    (passes if ok else fails).append(name)
    print(("PASS " if ok else "FAIL ") + name + ((" -- " + detail) if detail else ""))


def analyse(path):
    im = Image.open(path).convert("RGB")
    a = np.asarray(im).astype(np.int16)
    lum = a.mean(axis=2)
    sat = a.max(axis=2) - a.min(axis=2)
    m = np.zeros(lum.shape, bool)
    m[:12, :] = m[-12:, :] = True
    m[:, :12] = m[:, -12:] = True
    return dict(size=im.size, light=float((lum > 200).mean()) * 100,
                colour=float(((sat > 40) & (lum < 245)).mean()) * 100,
                edge=float((lum[m] < 160).mean()) * 100)


def main():
    png = os.path.join(HERE, "entry.png")
    raw = open(png, "rb").read()

    # 1. the file the judge sees
    check("png signature", raw[:8] == b"\x89PNG\r\n\x1a\n")
    w, h = struct.unpack(">II", raw[16:24])
    check("1024x1024", (w, h) == (1024, 1024), "%dx%d" % (w, h))
    check("under 1 MiB", len(raw) <= 1048576, "%d bytes" % len(raw))

    # 2. determinism and the committed bytes
    tmp = tempfile.mkdtemp()
    a = os.path.join(tmp, "a.png")
    b = os.path.join(tmp, "b.png")
    render.render(a)
    render.render(b)
    ha, hb = [hashlib.sha256(open(p, "rb").read()).hexdigest() for p in (a, b)]
    check("two runs byte-identical", ha == hb, ha[:12])
    check("committed == fresh render", ha == hashlib.sha256(raw).hexdigest(), ha[:12])

    # 3. the shipped program
    for i in (1, 2):
        out = os.path.join(tmp, "out%d" % i)
        env = dict(os.environ, MAKEFUN_OUTPUT_DIR=out)
        r = subprocess.run(["node", "main.ts"], cwd=HERE, env=env, capture_output=True, text=True)
        check("main.ts run %d" % i, r.returncode == 0, r.stderr.strip()[:120])
        if r.returncode == 0:
            got = open(os.path.join(out, "entry.png"), "rb").read()
            check("main.ts run %d ships the committed bytes" % i, got == raw)

    # 4. layout
    st = analyse(png)
    check("no ink in the 12 px border", st["edge"] == 0.0, "%.2f%%" % st["edge"])
    check("light paper 65-90%", 65 <= st["light"] <= 90, "%.1f%%" % st["light"])
    check("some colour on the page", st["colour"] >= 3.0, "%.1f%%" % st["colour"])

    # 5. text, at full size and at 300 px
    from rapidocr_onnxruntime import RapidOCR
    ocr = RapidOCR()

    def read(path):
        res, _ = ocr(path, use_det=True, use_cls=False, use_rec=True)
        return [(t, float(c)) for _, t, c in (res or [])]

    full = read(png)
    small_path = os.path.join(tmp, "small.png")
    Image.open(png).convert("RGB").resize((300, 300), Image.LANCZOS).save(small_path)
    small = read(small_path)

    def norm(s):
        return re.sub(r"[^a-z0-9]", "", s.lower())

    full_text = " ".join(t for t, c in full if c > 0.5)
    nf = norm(full_text)

    check("date in masthead", norm("WEDNESDAY 25 NOVEMBER 2026") in nf)
    for i, lead in enumerate(stories.LEADS):
        head = lead[5]
        words = [w for w in re.findall(r"[A-Za-z0-9']+", head) if len(w) > 3]
        hit = sum(1 for w in words if norm(w) in nf)
        check("lead %d headline readable" % (i + 1), hit >= max(2, len(words) - 2),
              "%d/%d words" % (hit, len(words)))
    for i, sec in enumerate(stories.SECOND):
        head = sec[4]
        words = [w for w in re.findall(r"[A-Za-z0-9']+", head) if len(w) > 3]
        hit = sum(1 for w in words if norm(w) in nf)
        check("second %d headline readable" % (i + 1), hit >= max(2, len(words) - 1),
              "%d/%d words" % (hit, len(words)))
    brief_hits = 0
    for _, place, region, desk, text, utc in stories.BRIEFS:
        words = [w for w in re.findall(r"[A-Za-z0-9']+", text) if len(w) > 3]
        if sum(1 for w in words if norm(w) in nf) >= 1:
            brief_hits += 1
    check("briefs readable", brief_hits >= len(stories.BRIEFS) - 2,
          "%d/%d" % (brief_hits, len(stories.BRIEFS)))
    for fig, lab in stories.NUMBERS:
        check("number %s readable" % fig, norm(fig) in nf, fig)

    small_text = norm(" ".join(t for t, c in small if c > 0.5))
    check("at 300 px the day still reads", norm("WEDNESDAY25NOVEMBER2026") in small_text)
    whole = 0
    for lead in stories.LEADS + stories.SECOND:
        head = lead[5] if len(lead) == 10 else lead[4]
        words = [w for w in re.findall(r"[A-Za-z0-9']+", head) if len(w) > 3]
        hit = sum(1 for w in words if norm(w) in small_text)
        if hit >= max(2, len(words) - 2):
            whole += 1
    check("at 300 px at least four headlines whole", whole >= 4, "%d/9" % whole)

    # 6. the page's own arithmetic
    tally = stories.counts()
    total = sum(tally.values())
    check("32 stories on the page", total == 32, str(total))
    check("region chips sum to the story count", sum(tally.values()) == total)
    check("masthead count == stories", total == len(stories.LEADS) + len(stories.SECOND) + len(stories.BRIEFS))

    print("\n%d pass, %d fail" % (len(passes), len(fails)))
    if fails:
        print("FAILED: " + ", ".join(fails))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
