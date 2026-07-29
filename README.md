# pixel-dungeon-portfolio

A two-page portfolio site:

- **Home** (`/`) is a modern, editorial-style portfolio page — big stacked
  serif headline, a grayscale portrait, a scrolling marquee of past
  companies, experience written up as case-study blocks, and grouped
  skills. On mobile the nav collapses into a hamburger menu; a "Dungeon"
  link fades into it a few seconds after load (and into a top-right button
  on desktop) linking through to the dungeon.
- **`/dungeon/`** is the original interactive experience: a top-down
  pixel-art dungeon with 5 glowing portals set into the back wall, each
  opening into a themed room for one project. You control a samurai sprite
  with WASD/arrow keys (or drag-to-move on touch) — walk up to a portal, or
  just click/tap/hover it, to step inside. A "Back to the boring portfolio"
  button returns to the home page.

Both pages are generated from the same underlying content, so editing one
file keeps them in sync.

- **Content** lives in Python (`content/frames.py`) — no HTML editing needed
  to add/edit a project. `content/portfolio.py` derives most of the modern
  portfolio page's content from `frames.py` automatically (experience,
  education); its resume-style grouped **Skills** section (AI-Augmented
  Testing & Automation / Programming Languages / Development Tools) is
  curated separately there, matching the SKILLS section of the actual
  resume rather than the flatter tag list `frames.py` uses for the
  dungeon's "About Me" room.
- **Build**: `build.py` uses Jinja2 to render everything into a static
  `dist/` folder (plain HTML/CSS/JS — this is what actually runs in the
  browser): `dist/index.html` (the portfolio home page), `dist/dungeon/`
  (the dungeon experience), and a shared `dist/static/`. It also
  auto-arranges however many portals you have across the back wall and
  assigns each one a themed archway/color.
- **Hosting**: free, via GitHub Pages at `elevenray.github.io`. This
  source repo is private; a small separate public repo holds only the
  built output for Pages to serve — see "Deploy" below.
- **License**: all rights reserved — see [LICENSE](LICENSE). The site is
  public so it can be visited, not so its code can be reused.

## Edit your content

Open [content/frames.py](content/frames.py) and edit the `SITE` dict and the
`FRAMES` list — one entry per portal/room (company, role, description, tags,
achievements, link). Add or remove entries freely; portal placement and
theming are computed automatically in `build.py` from however many entries
you have. The modern portfolio page (`content/portfolio.py`) pulls its
experience and education straight from this same list — the last entry in
`FRAMES` ("About Me") supplies the education, and every other entry becomes
one experience case-study block. Its Skills groups are edited directly in
`content/portfolio.py`.

## Preview locally

```bash
pip install -r requirements.txt
python build.py
python -m http.server -d dist 8000
```

Then open http://localhost:8000 in a browser.

## Deploy to GitHub Pages (private source, public deploy repo)

GitHub Pages on the Free plan can only publish from a **public** repo —
so a single-repo setup means the source (`build.py`, templates, commit
history) is necessarily public too. This project instead splits that in
two: **this repo stays private** and holds all the source; a second,
separate **public** repo named `elevenray.github.io` holds nothing but the
already-built `dist/` output, and that's what Pages actually serves. The
[LICENSE](LICENSE) covers the (unavoidably public) rendered site itself.

### One-time setup

1. **This repo**: rename it away from `elevenray.github.io` (Settings →
   General → Repository name — any name works, e.g. `elevenray-portfolio`)
   and make sure it's **private**.
2. **Create a new, separate public repo** named exactly
   `elevenray.github.io` — empty, no files needed. This is the one Pages
   will serve from.
3. In that new public repo, go to **Settings → Deploy keys → Add deploy
   key**, check **"Allow write access"**, and paste in this public key
   (already generated, its private half lives at
   `~/.ssh/elevenray_pages_deploy_key` — never commit that file):
   ```
   ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHCBdhJMGnH4LU8NbiI7WM+/7tKXy2kEAWdSnxC6Swbc elevenray-portfolio-pages-deploy
   ```
4. Back in **this** (renamed, private) repo, go to **Settings → Secrets
   and variables → Actions → New repository secret**, name it
   `PAGES_DEPLOY_KEY`, and paste in the *private* key. Get its contents by
   running this yourself in a terminal (not shown here on purpose):
   ```bash
   cat ~/.ssh/elevenray_pages_deploy_key
   ```
5. In the new public `elevenray.github.io` repo, go to **Settings → Pages**
   and set **Source** to **"Deploy from a branch"** → `main` → `/ (root)`.
6. Push to `main` on this (source) repo, or run the "Build and deploy
   site" workflow manually from the Actions tab. The workflow
   (`.github/workflows/deploy.yml`) runs `build.py`, then pushes the
   resulting `dist/` contents to the public repo's `main` branch.
7. Your site will be live at **https://elevenray.github.io** within a
   minute or two.

After that first setup, updating the site is just: edit
`content/frames.py` → commit → push to this repo. No need to run the
build or touch the public repo yourself.

## How it works

Both pages are pure CSS + vanilla JS, no frameworks.

### Home page (`static/js/portfolio.js`, `static/css/portfolio.css`)

- **Design**: 'Fraunces' (serif) for the big stacked hero headline and
  case-study pull-quotes, 'Archivo Black' for the wordmark/labels/skill
  pills, 'Inter' for body text — cream/near-black in light mode, inverted
  in dark, following `prefers-color-scheme`.
- **Nav**: sticky top bar. Below 640px it collapses into a hamburger button
  that toggles a dropdown (closes automatically when a link inside it is
  clicked); a "Dungeon" item fades into that dropdown 3 seconds after load.
  Above 640px the links stay visible and a "Dungeon" pill button fades in
  top-right after 5 seconds instead.
- **Marquee**: a CSS `@keyframes` loop scrolls past employers
  edge-to-edge; pauses under `prefers-reduced-motion`.
- **Experience**: each `frames.py` entry (other than "About Me") renders as
  a numbered case-study block — year/role/focus meta columns, an italic
  pull-quote summary, then the achievement bullets.
- **Mobile hero**: the portrait becomes a centered "pill" (a portrait-ratio
  image with `border-radius: 999px`, which clips to a stadium/capsule
  shape once it's taller than it is wide) and the Email/GitHub/LinkedIn
  buttons shrink onto a single row.

### Dungeon (`static/js/dungeon.js`, `static/css/style.css`)

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
