# Mud & Meadows — Project Memory

## Project Location
`C:\Users\quinn\Downloads\mudandmeadows\`

## Site Structure
- `mud-and-meadows.html` — Homepage (main entry point)
- `about.html` — About Us page
- `events.html` — All Events / Past Events masonry grid
- `calendar.html` — Upcoming Events calendar
- `images/` — All site images and videos
- `serve.js` — Local dev server (Node.js), runs on port 3000, serves from root dir
- `.claude/launch.json` — Preview server config

## How to Run
`node serve.js` or use the preview server named `mud-and-meadows`

## What Was Done This Session

### Image Extraction
- All base64-embedded images were extracted from HTML files into `images/` folder
- HTML files shrank from ~1MB each to ~20-44KB each

### Nav Logo Fix
- `about.html`, `events.html`, `calendar.html` were missing `.nav-logo-img` CSS rule
- Added `height:90px; width:90px; object-fit:contain;` to all three pages
- Fixed broken `href="index.html"` links → changed to `href="mud-and-meadows.html"`

### serve.js Updates
- Changed DIR from `extracted` folder to root (`__dirname`)
- Changed default route from `index.html` to `mud-and-meadows.html`

### Events Page (events.html) — Full Overhaul
Added video support (play button overlay + lightbox video player) and replaced all placeholder events with real ones:

| ID | Event | Image | Video |
|----|-------|-------|-------|
| 1 | Shamrock & Smoke (UPCOMING Mar 13) | southernwindsomd flyer | mud_and_meadows_1771711609 |
| 9 | Shamrock & Smoke — What's Included (UPCOMING) | southernwindsomd ticket details | mud_and_meadows_1771787868 |
| 2 | Valentine's Mommy & Me Pottery Brunch (Feb 8) | img_58232607.png | — |
| 3 | Tumbler Painting at The Sweet Little Shop | sweetlittleshop_tumblers.jpg ⚠️ MISSING | sweetlittleshop_tumbler.mp4 |
| 4 | Christmas Ornament Workshop (Dec 2024) | WordPress URL | — |
| 5 | Christmas Ornament Workshop #2 (Dec 2024) | WordPress URL | — |
| 6 | Galentines at Stone Silo (Feb 13) | mud_and_meadows_1768432250 flyer | galentines_recap.mp4 |
| 7 | Galentines — Ceramic Heart Dishes (Feb 13) | mud_and_meadows_1768432250 photo | mud_and_meadows_1768177414 |
| 8 | Ceramic Fish Plate at Hook & Vine (Feb 21) | mud_and_meadows_1768244378 | — |

### Homepage (mud-and-meadows.html) — Sweet Little Shop Section
- Replaced coffee cup placeholder with `images/sweetlittleshop_tumblers.jpg` (⚠️ STILL NEEDS TO BE ADDED)
- Added video support to slideshow (`buildSlides` now handles `type:'video'`)
- Sweet Little Shop slideshow: photo (slide 1) + `sweetlittleshop_tumbler.mp4` (slide 2)

## Images Folder Contents (`images/`)
| File | What It Is |
|------|-----------|
| img_5dea61d2.png | Mud & Meadows logo |
| img_58232607.png | Valentine's Mommy & Me brunch flyer |
| img_4ef6dfab.png | Old Shamrock & Smoke hat promo (replaced on events page) |
| img_79f914b5.png | About page — group outdoor photo |
| img_e3fc487a.png | About page — two girls with sunflowers |
| img_b39d2e1f.png | About page — girl with bouquet in car |
| img_4c07b1cf.png | About page — girl with cowboy hat |
| galentines_recap.mp4 | Galentines recap video ("speakeasy energy" caption) |
| sweetlittleshop_tumbler.mp4 | Tumbler painting event video |
| sweetlittleshop_recap.mp4 | Sweet Little Shop recap video ("Had a beautiful time painting") |
| mud_and_meadows_1768177414_...mp4 | Galentines promo/second video |
| mud_and_meadows_1768244378_...jpg | Hook & Vine Ceramic Fish Plate flyer (Feb 21) |
| mud_and_meadows_1768432250_...3810206561810369411_...jpg | Galentines at Stone Silo flyer |
| mud_and_meadows_1768432250_...3810206606664213223_...jpg | Galentines raw heart dishes photo |
| mud_and_meadows_1771711609_...mp4 | Shamrock & Smoke video |
| mud_and_meadows_1771787868_...mp4 | Shamrock & Smoke second video |
| southernwindsomd_...3837708149567102040_...jpg | Shamrock & Smoke ticket details |
| southernwindsomd_...3837708150221404294_...jpg | Shamrock & Smoke main flyer |

### Homepage Flower Farm Event (Session 2)
- Replaced "Christmas Ornaments" event row with "Flower Farm Winery & Pottery Painting"
- Cover photo: `images/flower_farm_plates.png` (sourced from OneDrive Screenshots)
- Popup slideshow: slide 1 = photo (`flower_farm_plates.png`), slide 2 = video (`flower_farm_winery.mp4`)
- Video copied from: `mud_and_meadows_1760285929_3741863902922785948_65621474870.mp4`
- Also saved: `images/flower_farm_poster.png` (Instagram collage promo image)
- Date: October 11, 2025 · 11:00 AM – 1:30 PM at Hope Flower Farm & Winery, Maryland

### Homepage Sweet Little Shop — Cover Video Update (Session 2)
- Copied `mud_and_meadows_1771711609_3837716150571096261_65621474870 (1).mp4` → `images/sweetlittleshop_cover.mp4`
- Replaced the static `<img>` in the Sweet Little Shop event row with `<video autoplay muted loop playsinline src="images/sweetlittleshop_cover.mp4">`
- Popup slideshow now uses only `sweetlittleshop_tumbler.mp4` (removed missing static image from media array)
- Rewrote 3 bullet points for cleaner/more accurate descriptions
- Fixed bullet point spacing: wrapped `<li>` text in `<span>` so `<em>` tags don't break the flex gap layout
- Added `.mp4` and `.webm` MIME types to `serve.js`
- Added `video` to `.event-img-wrap` hover CSS rules

## ⚠️ Outstanding TODOs
- **None currently** — `sweetlittleshop_tumblers.jpg` is no longer needed (replaced by `sweetlittleshop_cover.mp4` as the cover)

## Files That Should Go to Git
- `mud-and-meadows.html`
- `about.html`
- `events.html`
- `calendar.html`
- `images/` (all files)
- `serve.js`

## Files to EXCLUDE from Git
- `extracted/` (old working folder, superseded)
- `extract_images.py` (one-time tool, already run)
- `.claude/` (local Claude config)
