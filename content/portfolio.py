"""
Modern portfolio (site home page) content — derived from the same resume
data used by the dungeon experience (content/frames.py) so the two pages
never drift out of sync. Edit frames.py to update either page.
"""
from .frames import SITE, FRAMES

_ABOUT = FRAMES[-1]  # the "About Me" frame — reused here for bio/skills/education
_EXPERIENCE = FRAMES[:-1]

PROFILE = {
    "name": SITE["name"],
    "title": "Senior Technical Consultant",
    "location": "Santa Ana, CA",
    "email": SITE["email"],
    "github_username": SITE["github_username"],
    "linkedin": "linkedin.com/in/raymond-laurente",
    "summary": (
        "Senior Quality Engineer and Site Reliability Engineer focused on "
        "keeping releases on schedule and infrastructure reliable — always "
        "exploring how AI agents can make software testing and "
        "infrastructure work smarter."
    ),
    "photo": "static/images/profile.jpg",
    # Big stacked headline in the hero — the "specialties" a visitor sees
    # first, distinct from the full skill-tag list further down the page.
    "focus_areas": [
        "Quality Engineering",
        "Site Reliability",
        "AI-Augmented Testing",
        "Release Management",
    ],
    # Matches the SKILLS section of the current resume (grouped by
    # category), rather than the flat tag list frames.py uses for the
    # dungeon's "About Me" room.
    "skill_groups": [
        {
            "label": "AI-Augmented Testing & Automation",
            "tags": [
                "Agentic Workflow Orchestration",
                "Cursor AI",
                "GenCase (AI Test Case Generation)",
                "Playwright",
                "Selenium",
            ],
        },
        {
            "label": "Programming Languages",
            "tags": ["C++", "C", "Java", "Python", "SQL", "HTML", "CSS", "PHP", "Groovy", "Bash/Shell", "Git"],
        },
        {
            "label": "Development Tools",
            "tags": ["Adobe AEM", "Jenkins", "Splunk", "Dynatrace", "GitHub", "Akamai", "JIRA", "Visual Studio"],
        },
    ],
    "education": _ABOUT["achievements"],
    "experience": _EXPERIENCE,
    "companies": [job["company"] for job in _EXPERIENCE],
    "footer_note": SITE["footer_note"],
}
