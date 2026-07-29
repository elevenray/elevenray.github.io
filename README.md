# pixel-dungeon-portfolio

A two-page portfolio site:

- **Home** (`/`) is a modern, professional portfolio page — hero intro,
  skills, an experience timeline, and education/certifications. Five
  seconds after it loads, a "Learn more about me →" button fades in at the
  top right and links to the dungeon.
- **`/dungeon/`** is the original interactive experience: a top-down
  pixel-art dungeon with 5 glowing portals set into the back wall, each
  opening into a themed room for one project. You control a samurai sprite
  with WASD/arrow keys (or drag-to-move on touch) — walk up to a portal, or
  just click/tap/hover it, to step inside.

Both pages are generated from the same underlying content, so editing one
file keeps them in sync.

- **Content** lives in Python (`content/frames.py`) — no HTML editing needed
  to add/edit a project. `content/portfolio.py` derives the modern portfolio
  page's content from `frames.py` automatically.
- **Build**: `build.py` uses Jinja2 to render everything into a static
  `dist/` folder (plain HTML/CSS/JS — this is what actually runs in the
  browser): `dist/index.html` (the portfolio home page), `dist/dungeon/`
  (the dungeon experience), and a shared `dist/static/`. It also
  auto-arranges however many portals you have across the back wall and
  assigns each one a themed archway/color.
- **Hosting**: free, via GitHub Pages at `elevenray.github.io`.

## Edit your content

Open [content/frames.py](content/frames.py) and edit the `SITE` dict and the
`FRAMES` list — one entry per portal/room (company, role, description, tags,
achievements, link). Add or remove entries freely; portal placement and
theming are computed automatically in `build.py` from however many entries
you have. The modern portfolio page (`content/portfolio.py`) pulls its
skills, experience, and education straight from this same list — the last
entry in `FRAMES` ("About Me") supplies the skills/education, and every
other entry becomes one experience timeline item.

## Preview locally

```bash
pip install -r requirements.txt
python build.py
python -m http.server -d dist 8000
```

Then open http://localhost:8000 in a browser.

## Deploy to GitHub Pages (free)

1. Create a new **public** repo on GitHub named exactly `elevenray.github.io`.
2. Push this project to it:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/elevenray/elevenray.github.io.git
   git push -u origin main
   ```
3. In the repo, go to **Settings → Pages** and set **Source** to
   **GitHub Actions** (one-time setup).
4. The included workflow (`.github/workflows/deploy.yml`) runs `build.py`
   and publishes `dist/` automatically on every push to `main`.
5. Your site will be live at **https://elevenray.github.io** within a
   minute or two of the push.

After that first setup, updating the site is just: edit
`content/frames.py` → commit → push. No need to run the build yourself.

## How it works

Pure CSS + vanilla JS (`static/js/dungeon.js`, `static/css/style.css`), no
frameworks:

- **Moving around**: held WASD/arrow keys move the sprite freely in 8
  directions, with a matching walk-cycle animation and facing per direction.
  On touch, dragging the floor walks toward your finger instead.
- **Portals**: each one lights up and its name/role appears under the site
  title whenever the sprite walks close, or you hover/click/tap/focus it
  directly — no in-scene labels cluttering the room. Pressing Enter (or
  clicking/tapping) while near one steps through it.
- **Rooms**: stepping through a portal zooms/vignettes into a full project
  page, background-themed to match that portal's own color. "Back" (or
  Escape) returns you to the same spot in the dungeon.
- **The floor**: rendered as a separate tilted 3D plane (CSS `perspective` +
  `rotateX`) behind the portals/player/props, which stay flat and upright —
  the same "flat sprites over a 3D backdrop" trick HD-2D games use.
- **The art**: the floor/wall tileset, all 5 portal archways, the torches,
  the loot props, and the player's 8-direction walk cycle were generated
  with PixelLab and live under `static/images/`.

`prefers-reduced-motion` is respected throughout for accessibility.
