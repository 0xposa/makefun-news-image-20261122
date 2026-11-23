#!/usr/bin/env python3
"""
Sum up 22 November 2026's world news in one image.

Entry program for the make.fun bounty "Sum up 22 November's world news
in one image" (https://make.fun/bounty/news-image-20261122).

The program draws ONE poster-style PNG (1024x1024, < 1 MiB) summarising
the day's main world headlines and writes it to /output/entry.png
(falling back to ./output/entry.png when /output is not writable).

Fully deterministic: no network, no randomness, no clock reads that
affect the pixels -- two runs write identical bytes.

Headlines compiled 22-23 Nov 2026 from public reporting of Sunday
22 November 2026: the Associated Press (22 Nov 2026 wire items) and
Open Chronicle's "Global News Brief: Key World Developments,
November 22, 2026". See SUBMISSION.md for the per-story source list.

License: MIT (fonts bundled under the SIL Open Font License 1.1).
"""

import os
import sys

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "fonts")

W, H = 1024, 1024

# Palette -----------------------------------------------------------------
BG = (10, 17, 32)          # deep navy
PANEL = (19, 30, 51)       # card background
PANEL_EDGE = (38, 54, 84)
WHITE = (245, 247, 250)
MUTED = (158, 174, 196)
RED = (230, 57, 70)
GOLD = (244, 185, 66)
CYAN = (46, 196, 182)
ORANGE = (255, 140, 66)
GREEN = (110, 200, 120)
SKY = (96, 165, 250)


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


ANTON = "Anton-Regular.ttf"
BLACK = "Montserrat-Black.ttf"
XBOLD = "Montserrat-ExtraBold.ttf"
BOLD = "Montserrat-Bold.ttf"
SEMI = "Montserrat-SemiBold.ttf"
MED = "Montserrat-Medium.ttf"
REG = "Montserrat-Regular.ttf"


def text_w(draw, s, fnt):
    return draw.textlength(s, font=fnt)


def draw_tracked(draw, xy, s, fnt, fill, tracking=4):
    """Draw text with extra letter spacing (PIL has no tracking)."""
    x, y = xy
    for ch in s:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += text_w(draw, ch, fnt) + tracking
    return x


def wrap(draw, s, fnt, max_w):
    words, lines, cur = s.split(), [], ""
    for wd in words:
        trial = wd if not cur else cur + " " + wd
        if text_w(draw, trial, fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def build_image():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    M = 48                      # side margin
    CW = W - 2 * M              # content width

    # ---- header band ----------------------------------------------------
    d.rectangle([M, 40, M + 14, 94], fill=RED)
    d.text((M + 30, 44), "WORLD NEWS IN ONE IMAGE", font=font(ANTON, 44), fill=WHITE)
    date = "SUN  ·  22 NOVEMBER 2026"
    df = font(SEMI, 21)
    d.text((W - M - text_w(d, date, df), 58), date, font=df, fill=MUTED)
    d.line([M, 112, W - M, 112], fill=PANEL_EDGE, width=2)

    # ---- lead story ------------------------------------------------------
    draw_tracked(d, (M, 130), "TOP STORY — CLIMATE · ANTALYA, TÜRKIYE",
                 font(BOLD, 21), RED, tracking=3)
    lead = font(ANTON, 104)
    d.text((M, 160), "COP31 SUMMIT", font=lead, fill=WHITE)
    d.text((M, 272), "ENDS IN COLLAPSE", font=lead, fill=GOLD)
    sub = ("The UN climate summit in Antalya broke down after nearly 200 "
           "nations split over fossil fuels and climate finance — the talks "
           "ran into overtime and closed with no overarching deal.")
    y = 400
    for line in wrap(d, sub, font(REG, 25), CW):
        d.text((M, y), line, font=font(REG, 25), fill=(205, 214, 228))
        y += 34
    d.line([M, 512, W - M, 512], fill=PANEL_EDGE, width=2)
    draw_tracked(d, (M, 526), "ALSO TODAY", font(BLACK, 23), WHITE, tracking=5)

    # ---- story cards (2 cols x 3 rows) ------------------------------------
    cards = [
        ("UKRAINE WAR", SKY,
         "Ukrainian sea drones hit Russian warship in Libya",
         "Strike at Benghazi naval base (AP)"),
        ("IRAN · GULF", RED,
         "Tankers struck near Hormuz as Gulf tensions flare",
         "Bahrain: Iranian attack injures two at Sitra"),
        ("MYANMAR", ORANGE,
         "World court: Myanmar committed Rohingya genocide",
         "Rohingya refugees welcome the ICJ verdict"),
        ("US POLITICS", GOLD,
         "Democrats clinch a historic House majority",
         "At least 258 seats — largest since 1992 (AP)"),
        ("INDONESIA", CYAN,
         "Deadly fire tears through Banten candy factory",
         "Workers dead; dozens unaccounted for (AP)"),
        ("SPORT", GREEN,
         "49ers rout Vikings 35–10 in Mexico City",
         "Purdy throws three TD passes (AP)"),
    ]
    gap = 10
    card_w = (CW - gap) // 2
    card_h = 124
    top = 560
    for i, (tag, color, head, detail) in enumerate(cards):
        cx = M + (i % 2) * (card_w + gap)
        cy = top + (i // 2) * (card_h + gap)
        d.rounded_rectangle([cx, cy, cx + card_w, cy + card_h],
                            radius=12, fill=PANEL, outline=PANEL_EDGE, width=1)
        d.rectangle([cx, cy + 10, cx + 6, cy + 40], fill=color)
        draw_tracked(d, (cx + 20, cy + 10), tag, font(BOLD, 16), color, tracking=2)
        hy = cy + 34
        for line in wrap(d, head, font(BOLD, 23), card_w - 40)[:2]:
            d.text((cx + 20, hy), line, font=font(BOLD, 23), fill=WHITE)
            hy += 27
        d.text((cx + 20, cy + 96), detail, font=font(MED, 17), fill=MUTED)

    # ---- footer ------------------------------------------------------------
    fy = top + 3 * card_h + 2 * gap + 12
    foot = "ALSO: Russian strike near Kyiv kills at least 2 · Delta automation failure delays Atlanta flights"
    d.text((M, fy), foot, font=font(MED, 17), fill=MUTED)
    src = "Sources: AP · Open Chronicle Global News Brief — headlines of Sunday 22 Nov 2026"
    sf = font(SEMI, 17)
    d.text(((W - text_w(d, src, sf)) / 2, H - 42), src, font=sf, fill=(110, 126, 152))
    d.rectangle([0, H - 10, W, H], fill=RED)
    return img


def main():
    img = build_image()
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.png")
        img.save(out_path, format="PNG", optimize=True)
    except OSError:
        out_dir = os.path.join(HERE, "output")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.png")
        img.save(out_path, format="PNG", optimize=True)
    size = os.path.getsize(out_path)
    print(f"wrote {out_path} ({img.size[0]}x{img.size[1]}, {size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
