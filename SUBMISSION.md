# Submission — make.fun bounty "Sum up 22 November's world news in one image"

Status: **BUILT, NOT SUBMITTED.** Nothing has been uploaded to make.fun.
Prepared 2026-11-23 ~23:52 WITA for account **@raphael99**.
Sibling entry (same format, 23 Nov): `~/workspace/projects/makefun/news-image/`.

## Bounty (spec, verified from the requirements API by the parent agent)

- URL: https://make.fun/bounty/news-image-20261122
- Slug: `news-image-20261122`
- Prize: **$100, 50 paid places** — 1st $20, 2nd $12, 3rd $6, 4th–10th $2 each,
  11th–50th $1.20 each (same prize table as the 23 Nov sibling bounty).
- Deadline: **Tue 24 Nov 2026, 00:00 UTC = 08:00 WITA, 24 Nov 2026**
  (21,169 agents had entered when the board was mapped on 23 Nov).
- Task, verbatim essence: "Sum up the world's news of Sunday 22 November 2026
  in one image. Your entry is a program that writes one image to
  `/output/entry.png`."

### How it is run and scored

- The submitted **program** is run in make.fun's sandbox; it must write one
  image to `/output/entry.png`. **No network.** The program runs **twice and
  both runs must write the same bytes** (deterministic output required).
- An AI judge that can see images compares entries **two at a time** and
  picks the one that best sums up the day's world news; entries **rank by
  win rate**. The judge has **no news feed** — it judges only what the image
  itself shows, like a picture editor.

### Image constraints

- Whole **PNG or JPEG**, at most **1 MiB**, at most **1024 × 1024 px**.

### Exact submission format (deliverables)

1. **A public GitHub repository owned by your own GitHub account** (or a
   source bundle), **created after the competition opened**, under an
   **OSI-approved license**, with the program at **`main.ts` (Node 22) or
   `main.py` (Python 3.13) in the repository root**. (This entry draws the
   image with PIL — self-contained, no bundled raster image.)
2. **The AI coding-agent transcripts of the sessions that built it**,
   uploaded with each submission (the parent agent handles the bundle;
   `TRANSCRIPT.md` in this folder is the human-readable summary).
3. Submission is made by the account holder through make.fun's agent
   flow. The **last submission before the deadline is the final entry**.

## What to submit (this entry)

Push the contents of this folder as the root of a NEW public GitHub repo
(created after the competition opened):

| File | Role |
|---|---|
| `main.py` | The entry program (Python 3.13, PIL/Pillow only). Writes `/output/entry.png` (falls back to `./output/entry.png`). |
| `fonts/` | Anton + Montserrat TTFs (SIL OFL 1.1) bundled so rendering is identical in the sandbox. |
| `LICENSE` | MIT (OSI-approved). |
| `output/entry.png` | The generated image, for reference/preview (the sandbox regenerates it by running `main.py`). |
| `SUBMISSION.md` | This file. |
| `TRANSCRIPT.md` | Honest summary of the build session. |

### Verified properties of this build (2026-11-23)

- Output: **1024 × 1024 PNG, 127,125 bytes (~124 KiB, well under 1 MiB)**.
- Determinism verified: two consecutive runs of `main.py` produced
  identical bytes (md5 `f33e383f59de1c5a6955873fc819c8d7` both runs).
- No network calls, no randomness, no clock-dependent pixels.
- Output image visually checked by the builder (poster layout, no text
  overlap, no clipped lines, all headlines legible at full size). One
  iteration was needed: the footer "ALSO" strip initially overflowed the
  right edge and was shortened.

## The image

Poster layout: masthead "WORLD NEWS IN ONE IMAGE — Sun 22 November 2026",
lead story with oversized Anton headline, 3-line summary, then six story
cards (Ukraine War, Iran · Gulf, Myanmar, US Politics, Indonesia, Sport),
an "ALSO" strip and a source line.

### Headlines used, with sources

All are the main world headlines of **Sunday 22 November 2026**, compiled
from the Associated Press wire items dated 22 Nov 2026 and Open
Chronicle's *Global News Brief: Key World Developments, November 22,
2026*:

1. **LEAD — COP31 summit ends in collapse.** The U.N. COP31 climate
   conference in Antalya, Türkiye ended on Sunday without an overarching
   agreement after nearly 200 countries failed to resolve differences
   over fossil fuels and climate finance; the talks ran into a second
   day of overtime. — Open Chronicle Global News Brief (22 Nov 2026);
   The Russell Record daily headlines (22 Nov 2026); AP: "UN climate
   talks break down over bitter disagreements on fossil fuels"
   (22 Nov 2026).
2. **Ukrainian sea drones hit a Russian warship in Libya** — suspected
   Ukrainian maritime drones struck a Russian naval vessel docked at the
   Benghazi Naval Base in eastern Libya, per Libyan officials. —
   Associated Press (22 Nov 2026); Open Chronicle §02.
3. **Tankers struck near the Strait of Hormuz; Bahrain reports an
   Iranian attack** — separate maritime incidents involved projectiles
   near Hormuz, and Bahrain said an Iranian attack on a civilian
   industrial facility in Sitra injured two. — The Russell Record
   (22 Nov 2026); Open Chronicle §03; AP Mideast roundup (22 Nov 2026).
4. **World court rules Myanmar committed genocide against the Rohingya**
   — the International Court of Justice ruled that Myanmar committed
   genocide against its Rohingya minority; Rohingya refugees in
   Bangladesh welcomed the verdict. — KPFA / Pacifica Evening News
   (22 Nov 2026); Associated Press (22 Nov 2026).
5. **Democrats clinch a historic House majority** — at least 258 seats,
   the largest House majority for either party since 1992. —
   Associated Press (22 Nov 2026).
6. **Deadly fire at a Banten candy factory, Indonesia** — AP reported
   workers dead and 37 unaccounted for on 22 Nov; more remains were
   recovered later that day as the search continued. — Associated Press
   (22 Nov 2026).
7. **Sport: 49ers rout the Vikings 35–10 in Mexico City** — Brock Purdy
   threw three touchdown passes in San Francisco's win. — Associated
   Press (22 Nov 2026).
8. ALSO strip: **Russian attack near Kyiv kills at least 2** in an
   apartment building (Associated Press, 22 Nov 2026); **Delta
   automation-system failure delays flights in Atlanta** (Associated
   Press, 22 Nov 2026).

Source pages:
- https://openchronicle.org/2026/11/22/global-news-brief-key-developments-around-the-world-november-22-2026/
- https://www.russellrecord.com/?view=daily-headlines
- https://kpfa.org/episode/the-pacifica-evening-news-weekdays-november-22-2026/
- AP wire items dated 11/22/2026 via the AP Top Stories listing
  (tunein.com AP Top Stories) and AP wire mirrors.

## Remaining steps for the parent agent / Master (not done here)

1. Create the new public GitHub repo and push this folder's contents.
2. Submit via make.fun (account @raphael99) with the session transcript
   bundle, before **24 Nov 2026 08:00 WITA**.
3. A linked Solana wallet is required only to *claim* any prize, not to
   enter.
