# museum-portfolio

An interactive portfolio site: one large landscape frame centered on screen
at a time — move your mouse left/right to browse to the next one, click to
get pulled inside and see the project/company behind it. A museum bench with
a small silhouette sits below, tracking which piece you're in front of.

- **Content** lives in Python (`content/frames.py`) — no HTML editing needed
  to add/edit a project.
- **Build**: `build.py` uses Jinja2 to render everything into a static
  `dist/` folder (plain HTML/CSS/JS — this is what actually runs in the
  browser).
- **Hosting**: free, via GitHub Pages at `elevenray.github.io`.

## Edit your content

Open [content/frames.py](content/frames.py) and edit the `SITE` dict and the
`FRAMES` list — one entry per frame/room (company, role, description, tags,
achievements, link). Add or remove entries freely; the gallery and rooms are
generated from this list automatically.

### Adding screenshots/logos

Each frame has an `"image"` field. Drop a landscape screenshot or logo into
`static/images/` and point to it, e.g. `"image": "static/images/acme.png"`.
Frames are landscape (roughly 8:5) — a wide browser screenshot or a logo
centered on a plain background both work well. Leave `"image": ""` to fall
back to a plain gold-lit placeholder with the company name.

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

Pure CSS + vanilla JS (`static/js/gallery.js`, `static/css/style.css`), no
frameworks:

- **Browsing**: moving the mouse across the gallery divides it into one zone
  per frame; only the frame under the cursor is shown (others are fully
  hidden, not peeking) with a soft crossfade between them. Arrow buttons,
  the left/right arrow keys, and touch swipe all work too.
- **Stepping inside**: clicking a frame scales it up dramatically while a
  vignette closes in, then the matching "room" section fades in underneath.
  "Back to gallery" (or Escape) reverses it.
- **The bench**: stationary at the bottom, with a small silhouette that
  walks to line up with whichever frame is active. If you stay on one frame
  for more than 3 seconds, it sits down; moving to another frame stands it
  back up.

`prefers-reduced-motion` is respected throughout for accessibility.
