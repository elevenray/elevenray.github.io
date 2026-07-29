"""
Portfolio content. Edit this file to update the site — no HTML/CSS knowledge
needed. Run `python build.py` afterward (or just push to GitHub, the Actions
workflow rebuilds automatically) to regenerate the static site.
"""

SITE = {
    "title": "Raymond Laurente — Portfolio",
    "name": "Raymond Laurente",
    "tagline": "Step into the gallery.",
    "github_username": "elevenray",
    "email": "raymondlaurente@gmail.com",
    "footer_note": "Built with Python + Jinja2. Hosted free on GitHub Pages.",
}

# Each entry becomes one portal in the dungeon, and one room you step into
# when you enter it. Order here is left-to-right across the back wall.
# build.py auto-assigns each portal's position and archway/color theme based
# on this list's length and order — no per-frame layout fields needed here.
#
# `image` is currently unused (a leftover from an earlier design) — safe to
# ignore or remove.
FRAMES = [
    {
        "id": "frame-1",
        "image": "",
        "company": "Perficient — Innocean / Hyundai / LPL Financial",
        "role": "QA Lead Engineer & Senior Technical Consultant",
        "period": "May 2024 – Present",
        "summary": "Leading AI-augmented QA automation across distributed teams and multiple enterprise clients.",
        "description": (
            "Lead and mentor an offshore QA team, weaving AI agent-assisted "
            "workflows into daily test operations to keep sprint timelines "
            "and quality standards aligned across distributed contributors. "
            "Design comprehensive UAT scripts and define QA strategies for "
            "AI-driven projects, tackling challenges like data variability "
            "and model validation."
        ),
        "tags": ["Cursor AI", "Playwright", "Java", "GenCase", "Zephyr", "Agentic Workflows"],
        "achievements": [
            "Lead and mentor an offshore QA team, integrating AI agent-assisted workflows into daily operations.",
            "Design and deliver UAT scripts using AI-assisted authoring tools, accelerating script creation.",
            "Develop story-level automation with Starling/Playwright (Java), using Cursor AI to speed up test script generation.",
            "Orchestrate test case creation and execution using Zephyr and GenCase, an AI-driven test management tool.",
            "Define QA strategies for AI-driven projects, addressing data variability and edge-case handling.",
        ],
        "link": "",
        "link_label": "View project",
        "accent": "#c9a35c",
    },
    {
        "id": "frame-2",
        "image": "",
        "company": "Perficient — Ford",
        "role": "Site Reliability Engineer & Senior Technical Consultant",
        "period": "Jun 2021 – Present",
        "summary": "Keeping deployment, monitoring, and log-analysis infrastructure reliable for a $48.5B automotive company.",
        "description": (
            "Partner with Ford's clients and microservices teams in Irvine, "
            "CA to optimize and maintain critical infrastructure, "
            "implementing deployment pipelines across Adobe AEM "
            "environments and building Splunk dashboards to monitor "
            "security events and system performance."
        ),
        "tags": ["Jenkins", "Groovy", "Splunk", "Dynatrace", "Adobe AEM", "JIRA"],
        "achievements": [
            "Automated code deployment using Jenkins and Groovy scripts, cutting manual deployment effort by 90%.",
            "Managed and configured Splunk for log analysis, reducing error rates by 60% through proactive monitoring.",
            "Built Splunk dashboards tracking security events, authentication attempts, and access violations.",
            "Used Dynatrace to monitor system performance and get ahead of bottlenecks and downtime risk.",
            "Conducted risk assessments of system changes via JIRA to minimize impact on availability.",
        ],
        "link": "",
        "link_label": "View project",
        "accent": "#7f9c8c",
    },
    {
        "id": "frame-3",
        "image": "",
        "company": "Optimus Learning",
        "role": "Software Developer Intern",
        "period": "Dec 2019 – Nov 2020",
        "summary": "Built the company website from the ground up and tutored the next generation in code.",
        "description": (
            "Led development of Optimus Learning's website using HTML, "
            "CSS, and JavaScript/PHP, then implemented SEO improvements "
            "that grew traffic by 30%. Also taught middle schoolers Math "
            "and Python."
        ),
        "tags": ["HTML", "CSS", "PHP", "JavaScript", "SEO"],
        "achievements": [
            "Led development of the company website, creating a polished, user-friendly interface.",
            "Implemented SEO algorithms, increasing website traffic by 30%.",
            "Instructed middle school students in Math and Python.",
        ],
        "link": "",
        "link_label": "View project",
        "accent": "#8c7fa0",
    },
    {
        "id": "frame-4",
        "image": "",
        "company": "Independent Projects",
        "role": "Web Layer: Site Crawler & Canonical Tag Scraper",
        "period": "Aug 2022 – Sep 2022",
        "summary": "A multithreaded Python crawler built to map site structure and validate canonical tags at scale.",
        "description": (
            "Built a Python-based web crawler with multithreading to "
            "efficiently scrape unsecured website domains, using a "
            "search-tree algorithm to extract every link from HTML source "
            "and analyze site structure, plus scrape canonical tags for "
            "accuracy review."
        ),
        "tags": ["Python", "Multithreading", "Web Scraping"],
        "achievements": [
            "Built a multithreaded crawler bot for comprehensive site data collection.",
            "Designed a search-tree algorithm to extract all links from HTML source code.",
            "Added canonical tag scraping to improve data accuracy and relevance.",
        ],
        "link": "",
        "link_label": "View project",
        "accent": "#b0654f",
    },
    {
        "id": "frame-5",
        "image": "static/images/profile.jpg",
        "company": "About Me",
        "role": "",
        "period": "",
        "summary": "QA Lead Engineer & Site Reliability Engineer based in Santa Ana, CA.",
        "description": (
            "Always exploring how AI agents can make software testing and "
            "infrastructure work smarter. Reach me at "
            "raymondlaurente@gmail.com, on LinkedIn "
            "(linkedin.com/in/raymond-laurente), or at raymondlaurente.com."
        ),
        "tags": ["Python", "C++", "Java", "SQL", "Git", "AI Test Automation"],
        "achievements": [
            "B.S. Computer Science — California State University, Fullerton",
            "A.S. Science & Mathematics (Honors) — Fullerton College",
            "Certified SAFe 5 Agilist (Scaled Agile Inc.)",
        ],
        "link": "mailto:raymondlaurente@gmail.com",
        "link_label": "Email me",
        "accent": "#b0654f",
    },
]
