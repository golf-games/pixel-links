#!/usr/bin/env python3
"""Builds index.html: one self-contained file with the fonts and all the game code inlined.

Usage:  python3 build.py
Needs Python 3 only (no packages). Edit files in src/, then run this to refresh index.html.
"""
import base64
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "src"
ORDER = ["courses.js", "data.js", "world.js", "render3d.js", "art.js", "engine.js", "ui.js", "club.js", "travel.js", "pool.js", "darts.js", "casino.js", "online.js"]

shell = (SRC / "shell.html").read_text(encoding="utf-8")
font = base64.b64encode((ROOT / "assets" / "font.woff2").read_bytes()).decode()
def face(fam, weight, fn, style="normal"):
    data = base64.b64encode((ROOT / "assets" / fn).read_bytes()).decode()
    return ('@font-face{font-family:"%s";font-style:%s;font-weight:%s;font-display:block;'
            'src:url(data:font/woff2;base64,%s) format("woff2")}' % (fam, style, weight, data))
font_css = ('<style>@font-face{font-family:"Press Start 2P";font-style:normal;font-weight:400;'
            'font-display:block;src:url(data:font/woff2;base64,' + font + ') format("woff2")}'
            + face("Barlow", 500, "bar500.woff2") + face("Barlow", 600, "bar600.woff2") + face("Barlow", 700, "bar700.woff2")
            + face("Barlow Condensed", 600, "barc600.woff2") + face("Barlow Condensed", 700, "barc700.woff2")
            + face("Barlow Condensed", 800, "barc800i.woff2", "italic") + '</style>\n')

# swap the Google Fonts links for the embedded font so the game works offline
shell = re.sub(r'<link rel="preconnect"[^\n]*\n<link rel="preconnect"[^\n]*\n<link href="https://fonts[^\n]*\n',
               lambda m: font_css, shell)
if "fonts.googleapis" in shell:
    raise SystemExit("Could not find the font links in src/shell.html")

js = "\n".join((SRC / name).read_text(encoding="utf-8") for name in ORDER)

# Online leaderboards: bake in your Supabase project if these environment variables are set (the GitHub workflow passes
# them from repository secrets). Without them the game asks for the URL and key on its ONLINE screen instead.
import os
for var, placeholder in (("SUPABASE_URL", "__SUPABASE_URL__"), ("SUPABASE_PUBLISHABLE_KEY", "__SUPABASE_PUBLISHABLE_KEY__")):
    val = os.environ.get(var, "").strip() or (os.environ.get("SUPABASE_ANON_KEY", "").strip() if var == "SUPABASE_PUBLISHABLE_KEY" else "")
    if val:
        if not re.fullmatch(r"[A-Za-z0-9_.:/\-]+", val):
            raise SystemExit(f"{var} contains unexpected characters")
        js = js.replace(placeholder, val)
        print(f"Using {var} from the environment")
if "/*JS*/" not in shell:
    raise SystemExit("src/shell.html is missing the /*JS*/ placeholder")

out = ROOT / "index.html"
out.write_text(shell.replace("/*JS*/", js), encoding="utf-8")
print(f"Built {out.name}: {out.stat().st_size:,} bytes")
