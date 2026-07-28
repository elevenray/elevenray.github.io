#!/usr/bin/env python3
"""
Static site generator for the pixel-dungeon portfolio site.

Reads content from content/frames.py, renders templates/index.html.j2 with
Jinja2, and writes the finished static site (HTML/CSS/JS only — nothing
executes server-side) to dist/. That dist/ folder is what gets deployed to
GitHub Pages.

Usage:
    python build.py
"""
import hashlib
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from content.frames import SITE, FRAMES

ROOT = Path(__file__).parent
TEMPLATES_DIR = ROOT / "templates"
STATIC_DIR = ROOT / "static"
DIST_DIR = ROOT / "dist"


def file_hash(path):
    return hashlib.sha1(path.read_bytes()).hexdigest()[:10]


# Each portal's archway image paired with a matching accent color (picked to
# match that archway's own glow), so the portal you see and the room/UI color
# it opens into are always the same — independent of content/frames.py's own
# "accent" field, which is unrelated per-project branding, not a portal skin.
ARCHWAY_THEMES = [
    ("static/images/cave/archway-green.png", "#4ade80"),
    ("static/images/cave/archway-blue.png", "#4fd2e8"),
    ("static/images/cave/archway-orange.png", "#ff8c3c"),
    ("static/images/cave/archway-purple.png", "#b06bf0"),
    ("static/images/cave/archway-gold.png", "#f5c451"),
]


def layout_portals(frames):
    """Arrange N portals along a shallow concave arc across the back of the
    dungeon room, evenly spaced left-to-right with the outer ones pulled
    slightly toward the player. Returns frames with portal_x/portal_y (% of
    the room) set, so content/frames.py can stay pure content."""
    n = len(frames)
    for i, frame in enumerate(frames):
        t = 0.5 if n == 1 else i / (n - 1)
        frame["portal_x"] = round(10 + 80 * t, 1)
        # Anchored low enough that ~30% of each archway's own height overlaps
        # the floor (see .back-wall's height in style.css) instead of sitting
        # flush against a hard wall/floor seam. Kept nearly uniform across
        # portals (not tied to the x-arc) so every one overflows by the same
        # amount, not just the outer ones.
        frame["portal_y"] = round(48 + 3 * (2 * t - 1) ** 2, 1)
        archway, portal_color = ARCHWAY_THEMES[i % len(ARCHWAY_THEMES)]
        frame["archway"] = f"{archway}?v={file_hash(ROOT / archway)}"
        frame["portal_color"] = portal_color
    return frames


def build():
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir(parents=True)

    shutil.copytree(STATIC_DIR, DIST_DIR / "static")

    # Cache-bust CSS/JS so browsers (and this project's own preview server)
    # never serve a stale copy after content changes.
    asset_version = {
        "css": file_hash(STATIC_DIR / "css" / "style.css"),
        "js": file_hash(STATIC_DIR / "js" / "dungeon.js"),
    }

    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)))
    template = env.get_template("index.html.j2")
    html = template.render(site=SITE, frames=layout_portals(FRAMES), asset_version=asset_version)
    (DIST_DIR / "index.html").write_text(html, encoding="utf-8")

    print(f"Built site into {DIST_DIR}")


if __name__ == "__main__":
    build()
