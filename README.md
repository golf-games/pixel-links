# Pixel Links Golf

A pixel-art golf game that runs in the browser. One HTML file, no install, no server.

## Play

Open `index.html` in Chrome, Edge, Firefox or Safari. That's it.

Progress saves in the browser you play in (local storage). To move a save to another device, use **Settings → Export code** and **Import code**.

## What's in here

| Path | What it is |
|---|---|
| `index.html` | The built game. Open this to play. |
| `src/shell.html` | Page layout and all CSS. The game code is inserted at `/*JS*/`. |
| `src/courses.js` | Every course: scorecards, hole shapes, hazards, colours. |
| `src/data.js` | Clubs, golfers, caddies, carts, balls, events, trophies, weather, saves, sound. |
| `src/world.js` | Hole generation: fairways, greens, bunkers, water, trees, backdrops. |
| `src/render3d.js` | Drawing: sky, ground, golfers, caddies, carts, poses and celebrations. |
| `src/art.js` | Shop icons, balls and trophies. |
| `src/engine.js` | Ball physics, swing, caddie advice, scoring, replays, practice, camera. |
| `src/ui.js` | Menus, HUD, shop, Golf NZ app, events, tournaments, season. |
| `src/club.js` | Clubhouses: outside buildings, the walk-around room, bar, TV, members, prize giving. |
| `src/online.js` | Online leaderboards through Supabase (off until you connect a project). |
| `supabase/schema.sql` | The database table and privacy rules for online leaderboards. |
| `docs/ONLINE-LEADERBOARDS.md` | Step-by-step setup for online leaderboards. |
| `docs/GITHUB-PRO-GOOGLE.md` | Private repo on GitHub Pro + Google sign-in for several Google accounts. |
| `.github/workflows/pages.yml` | Optional: builds the game and publishes it with GitHub Pages. |
| `src/travel.js` | Flights abroad, the (fictional) Amalfi Jet Club card, its lounge and the in-flight scene, and the cheaper AirNZ Koru card (half-price flights). |
| `assets/bar*.woff2`, `assets/barc*.woff2` | Barlow and Barlow Condensed (UI and HUD fonts). |
| `tools/` | Playwright screenshot and test scripts used during development (edit the file paths before use). |
| `assets/font.woff2` | The Press Start 2P pixel font (see Credits). |
| `build.py` | Rebuilds `index.html` from `src/` and `assets/`. |

## Making changes

1. Edit files in `src/`.
2. Run `python3 build.py` (Windows: `py build.py`).
3. Open `index.html` to test.
4. Commit and push.

The JavaScript files are joined in this order: courses, data, world, render3d, art, engine, ui, club, travel, pool, darts, casino, online. They share globals, so later files can use anything defined earlier.

## Credits and notes

- Fonts: **Press Start 2P** by CodeMan38 and **Barlow / Barlow Condensed** by Jeremy Tribby, both under the SIL Open Font License 1.1 (https://openfontlicense.org). Keep these credits if you share the game.
- Real course scorecards, real tour players, and real brand names (balls, carts, clubs) are used for personal fun. Hole layouts are imagined. Hemi Walker is a fictional player.
- This repository is private and for personal use. If you ever make it public or share the game, swap out real people, brands and club names first.
