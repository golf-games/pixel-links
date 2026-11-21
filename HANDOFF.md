# Pixel Links Golf: handoff for a new chat

## How to use this

1. Start a new chat and attach `pixel-links-golf-project.zip`. Also attach `pixel-links-golf-TEST.html` if you want the test copy.
2. Paste everything in the **Prompt** section below as your first message.
3. Add the changes you want after the prompt, or send them in a second message.

---

## Prompt (copy from here)

I'm continuing work on my browser golf game, **Pixel Links Golf**, from a previous chat. The attached zip is the full project. Unzip it, read `HANDOFF.md` (this file) and `README.md`, then look over the code before changing anything.

**How the project works**
- It builds to one self-contained file, `index.html`, with all JavaScript and fonts inlined. It runs from a plain file with no server.
- Edit the files in `src/`, then run `python3 build.py` to rebuild `index.html`.
- `src/shell.html` holds the page layout and all the CSS. The JavaScript is inserted at the `/*JS*/` marker.
- The JavaScript files are joined in this order and share globals: courses, data, world, render3d, art, engine, ui, club, travel.
- The game is live on my private GitHub repo. When a version is done, send me the new `index.html`; I upload it myself. Also publish the build as a private artifact so I can test it in the chat.
- If I ask for a test setup (an Augusta invite, a handicap of 0, and so on), put it **only in the artifact copy**, as a one-time script added before `</body>`. Never put test changes in the `index.html` I put on GitHub.

**How I like to work**
- Be direct and honest, not agreeable. Tell me when I'm wrong and why. Rate ideas honestly out of 10. Say when you're unsure.
- I'm in New Zealand.
- I send long lists of changes. Work through all of them, test with screenshots, and tell me plainly what you couldn't do or did differently.
- Keep in-game text short and simple. Make things look modern and polished, and don't make it laggier.

**Where things are**

| File | What's in it |
|---|---|
| `src/courses.js` | Every course, built with `H()`: hole specs, palettes (`pal`), backdrop layers (`bd`), tree types, and flags like `ocean`, `cliffs`, `abroad`, `invite`, `memReq`, `ticket`, `fee`, `member`. |
| `src/data.js` | Clubs, golfers (`GOLFERS` with unlock rules in `GREQ`), caddies, carts, balls, items, gear, celebrations, `EVENTS`, achievements (`ACH`), weather, save/load and migrations (`applySave`), and the handicap system (`calcIndex`, `courseHcp`, `strokeAlloc`). |
| `src/world.js` | Hole generation (`genHole`): the grid of terrain types `T.*`, trees, hills, the azaleas at Augusta, perimeter trees, the cliff-shade and surf pass for Cape, and the coastline trace (`h.coast`, currently unused). Also the hole texture (`renderHole`) and backdrop layers. |
| `src/render3d.js` | The camera and projection (`proj`, `CAM`); the sky and backdrops (`drawSky`, which draws the Cape cliffs); the ground (`drawGround`, a per-pixel flat-plane raycast, the biggest performance cost). Also the vector characters: `drawGolferSide` and `drawGolferFront`, with their poses (`sidePose`, `frontPose`, the `walkPose` walk cycle, the `KF` keyframes), `charFx`, the carts (`drawCart`, the three-seat `'trio'` Augusta cart, the Maybach), and the trolley. |
| `src/art.js` | Shop icons, balls (including `drawBallHero`), trophies (drawn smooth at 3×), bar food and drink pictures (`drawFoodIcon`). |
| `src/engine.js` | `applyRes`, the main state object `G`, ball physics (`stepBall`, `rangeHit` for the range nets and bay). Also: the swing, the hole flow (`holeComplete`, `finishRound`, which includes the handicap maths, events and tournaments), and the cart ride or walk between shots (`startTravel`). Hemi's guest round is `genHemiHole` (every shot planned), `hemiNext` and `updateGuest`. Also the practice range (`startPractice`), the camera, `renderFrame`, the minimap and wind panel, and the colour grade (`drawGrade`). |
| `src/ui.js` | Screens are `SCR.*` and actions are `ACT.*` (buttons use `data-a`); `showScreen`, `hydrate` (draws `data-spr` and `data-thumb` canvases), and the HUD (`buildHUD`, `updateHUD`). Also the tournaments: `tournEnter`, `tournDeskHTML`, `prizeCeremony`, with the data side `tournNew`, `tournTable` and `botRound` in data.js. Also the events page, the shop (`shopItems`), the player card (with the APPEARANCE editor, `lookHTML`) and the Golf NZ phone app. `resize` sets a variable game width: `VW` runs from 480 to 650, `VH` is fixed at 270. |
| `src/club.js` | Clubhouses: `CH_STYLE` per course (outside, inside, menu, and `lux` 0–3 for how grand the room is). The walk-around room (`openClubhouse`, `drawClubhouse`, `updateClubhouse`); walking (`chWalkTo`, arrow and A/D keys). The bar: `chBarMenu`, `chServe` with the pour and hand-over animation, and `eatPose`/`foodInHand` (bite, chew, swallow). Shouting the bar is `chParty`. Also: the TV, drone flyovers from `chSnapStart`/`chSnapStep` plus ad breaks from `chTvAd`; what members say (`chLine`, `roundTalk`, which is honest about your last round); Jacob Beach at Ngahinapouri; the honours board; and the Augusta trial scene. |
| `src/travel.js` | Flights: `flightCost` (paid every trip, 20% off for members) and `hasJet`. The fictional Amalfi Jet Club card and the cheaper AirNZ Koru card (half-price flights, 15,000) (`JET`, `drawJetCard`), the lounge scene (`openJetOffice`, `SCR.office`, `drawOffice`) and the in-flight scene (`startFlight`, `drawFlight`). |
| `tools/` | Playwright scripts (Python, Chrome) for screenshots, profiling and flow tests. They point at `/home/claude/pixel-links-golf.html`; change that path before using them. |

**Rules and systems already in place (don't break these)**
- **Difficulty:** skill uses `skU()`. It's hard at the start and gets easier with better golfers, caddies and gear. Rory McIlroy with every buff should play about like the old easy game.
- **Handicap:** follows the World Handicap System.
  - Score differentials use net double bogey as the worst score per hole.
  - 9-hole rounds use the 2024 expected-score rule.
  - Soft and hard caps, and the exceptional-score reduction, apply.
  - 3 rounds are needed for a first index (my rule).
  - Lower is better; "+2.0" is better than scratch.
- **Saves:** the save version is 6. The v6 migration no longer resets handicaps; it only withdraws Augusta invites.
- **Augusta:**
  - Invite: win an event while your handicap is below 0 (`stats.plusWins`). Hemi Walker then messages you in the Golf NZ app.
  - The guest round with Hemi is free.
  - After it there's a handshake with the Chairman, and Augusta opens.
  - Membership needs a +2.0 handicap.
- **Clubhouses:** you can go in if you're a member, straight after a round there (from the scorecard), or during an event.
- **Membership:** needs 6 holes played at that course (`save.holesAt`).
- **Events:** tiered (Club, Regional, National, International, Major); some are 2 rounds with a cut. You sign in at the clubhouse tournament desk; prize giving happens there after the last round. Jacob Beach (idx 0.8) plays every Ngahinapouri event.
- **Prices:** bar prices are realistic, in local currency.
- **Hole in one:** you must shout the bar before your next round.
- **Brand rule:** don't copy real companies' logos, designs or offices, and don't draw real people. That's why the jet club and its founder are made up. Real product names as plain text in the shop are fine.

**Known issues and ideas for next time**
1. **Characters:** the players and caddies are still flat vector shapes. The biggest visual gap is a proper character art pass: high-detail sprites or a much better vector model.
2. **Performance:** the ground raycast (`drawGround`, about 45 ms per frame in headless software rendering) is the main cost. Adaptive quality steps the ground resolution and the canvas size down on slow devices. An expensive rim-light effect is turned off (`save.settings.rimfx`).
3. **Cape Kidnappers:** the ground is flat, so the cliffs can't truly drop away. The distant cliffs are a backdrop layer; the sea under the cliffs is shaded with surf. 3D cliff faces (`drawCliffs`) were tried and turned off. Real elevation would need a heightfield raycast.
4. **Walking scene:** it plays between shots (where the cart ride is), not between holes.
5. **Putting:** could still look better (camera and stroke). The flag is now laid on the green while putting.
6. **Celebrations and caddie gestures:** hands near the chest now hang their elbows naturally. A few celebrations could still use polish.

My new requests are below (or in my next message).

---

## Files in this handoff

- **`pixel-links-golf-project.zip`:** the whole project (`src/`, `assets/`, `build.py`, `index.html`, `README.md`, `HANDOFF.md`, `tools/`).
- **`pixel-links-golf-TEST.html`:** the artifact test build, which sends one fresh Augusta invite. For testing only; don't put it on GitHub.
- **`index.html`** in the zip is the clean build for GitHub (v29).
