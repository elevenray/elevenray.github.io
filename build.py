#!/usr/bin/env python3
"""
Static site generator for the museum-portfolio site.

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


def build():
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir(parents=True)

    shutil.copytree(STATIC_DIR, DIST_DIR / "static")

    # Cache-bust CSS/JS so browsers (and this project's own preview server)
    # never serve a stale copy after content changes.
    asset_version = {
        "css": file_hash(STATIC_DIR / "css" / "style.css"),
        "js": file_hash(STATIC_DIR / "js" / "gallery.js"),
    }

    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)))
    template = env.get_template("index.html.j2")
    html = template.render(site=SITE, frames=FRAMES, asset_version=asset_version)
    (DIST_DIR / "index.html").write_text(html, encoding="utf-8")

    print(f"Built site into {DIST_DIR}")


if __name__ == "__main__":
    build()
