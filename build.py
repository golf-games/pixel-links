#!/usr/bin/env python3
"""Builds index.html: one self-contained file with the font and all the game code inlined.

Usage:  python3 build.py
Needs Python 3 only (no packages). Edit files in src/, then run this to refresh index.html.
"""
import base64
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "src"
ORDER = ["courses.js", "data.js", "world.js", "render3d.js", "art.js", "engine.js", "ui.js"]

shell = (SRC / "shell.html").read_text(encoding="utf-8")
font = base64.b64encode((ROOT / "assets" / "font.woff2").read_bytes()).decode()
font_css = ('<style>@font-face{font-family:"Press Start 2P";font-style:normal;font-weight:400;'
            'font-display:block;src:url(data:font/woff2;base64,' + font + ') format("woff2")}</style>\n')

# swap the Google Fonts links for the embedded font so the game works offline
shell = re.sub(r'<link rel="preconnect"[^\n]*\n<link rel="preconnect"[^\n]*\n<link href="https://fonts[^\n]*\n',
               lambda m: font_css, shell)
if "fonts.googleapis" in shell:
    raise SystemExit("Could not find the font links in src/shell.html")

js = "\n".join((SRC / name).read_text(encoding="utf-8") for name in ORDER)
if "/*JS*/" not in shell:
    raise SystemExit("src/shell.html is missing the /*JS*/ placeholder")

out = ROOT / "index.html"
out.write_text(shell.replace("/*JS*/", js), encoding="utf-8")
print(f"Built {out.name}: {out.stat().st_size:,} bytes")
