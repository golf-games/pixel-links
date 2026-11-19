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
| `src/ui.js` | Menus, HUD, shop, Golf NZ app, events, season. |
| `assets/font.woff2` | The Press Start 2P pixel font (see Credits). |
| `build.py` | Rebuilds `index.html` from `src/` and `assets/`. |

## Making changes

1. Edit files in `src/`.
2. Run `python3 build.py` (Windows: `py build.py`).
3. Open `index.html` to test.
4. Commit and push.

The JavaScript files are joined in this order: courses, data, world, render3d, art, engine, ui. They share globals, so later files can use anything defined earlier.

## Credits and notes

- Font: **Press Start 2P** by CodeMan38, licensed under the SIL Open Font License 1.1 (https://openfontlicense.org). Keep this credit if you share the game.
- Real course scorecards, real tour players, and real brand names (balls, carts, clubs) are used for personal fun. Hole layouts are imagined. Hemi Walker is a fictional player.
- This repository is private and for personal use. If you ever make it public or share the game, swap out real people, brands and club names first.
