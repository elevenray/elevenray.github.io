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
        "company": "Perficient — LPL Financial",
        "role": "Senior Quality Engineer & Senior Technical Consultant",
        "period": "Oct 2025 – Present",
        "summary": "Keeping 42+ releases on schedule across five concurrent release types by leading a distributed QA team and AI-driven workflows.",
        "description": (
            "Lead and mentor a distributed offshore QA team, embedding AI "
            "agent-assisted workflows into daily operations. Migrated the "
            "team from Blackbird/Selenium to Starling/Playwright (Java) and "
            "built out AI harness engineering — orchestrating Cursor AI "
            "agents and custom skills across parallel test-development "
            "tracks."
        ),
        "tags": ["Cursor AI", "Playwright", "Javascript", "Zephyr", "GenCase", "AI Harness Engineering"],
        "achievements": [
            "Kept 42 releases on schedule since October 2025 across five concurrent release types (Primary, RAD, Support, Express, Emergency) — including a monthly Primary release with 500+ changes — by leading and mentoring a distributed offshore QA team and embedding AI agent-assisted workflows into daily operations.",
            "Drove migration of the client's automation stack from Blackbird/Selenium to Starling/Playwright, moving the suites from JavaScript to TypeScript for stronger type safety and lower-flake execution.",
            "Build and maintain end-to-end UI and API test automation in TypeScript, integrated into CI so regression runs on every build.",
            "Improved test case traceability and execution efficiency by ~90% across parallel test tracks by orchestrating work in Zephyr and GenCase, an AI-driven test management platform.",
            "Strengthened defect visibility and resolution speed by partnering closely with product managers, developers, and business stakeholders across the sprint cycle.",
            "Built QA strategies tailored to AI-driven projects, addressing data variability, model validation, and edge-case handling.",
        ],
        "link": "",
        "link_label": "View project",
        "accent": "#c9a35c",
    },
    {
        "id": "frame-2",
        "image": "",
        "company": "Perficient — Hyundai / Innocean",
        "role": "QA Lead Engineer & Senior Technical Consultant",
        "period": "May 2024 – Dec 2025",
        "summary": "Led QA for HeyHyundai, the AI-powered chat assistant on Hyundai's website, from black-box testing through production.",
        "description": (
            "Led and mentored a QA team conducting black-box testing of "
            "HeyHyundai, designing test strategies to validate model "
            "behavior — including personalization, memory, and caching — "
            "without visibility into the underlying implementation."
        ),
        "tags": ["Cypress", "AI-Assisted Authoring", "Black-Box Testing", "HeyHyundai"],
        "achievements": [
            "Cut UAT script authoring time by ~80% (from ~2 hours to ~20 minutes per script) for client-side validation cycles by using AI-assisted authoring tools to generate scripts that fully verified business requirements before sign-off.",
            "Led and mentored a QA team conducting black-box testing of HeyHyundai, the AI-powered chat assistant on Hyundai's website, designing test strategies to validate model behavior without visibility into underlying implementation.",
            "Designed QA strategies to test HeyHyundai's personalization and memory behavior, addressing caching and data ID handling by generating fresh browser profiles to validate how the AI retained and recalled user data across sessions.",
            "Built a Cypress automation script to validate the AI-driven dynamic personalization engine that reordered vehicle page components in real time to guide users closer to purchase — reducing manual testing effort by ~50%.",
            "Supported 4 major production releases of HeyHyundai over the engagement by aligning QA strategy and defect resolution across cross-functional teams.",
        ],
        "link": "",
        "link_label": "View project",
        "accent": "#8c7fa0",
    },
    {
        "id": "frame-3",
        "image": "",
        "company": "Perficient — Ford",
        "role": "Site Reliability Engineer & Senior Technical Consultant",
        "period": "Jun 2021 – May 2024",
        "summary": "Kept deployment, monitoring, and log-analysis infrastructure reliable for a $48.5B automotive company.",
        "description": (
            "Maintained performance and reliability of critical "
            "infrastructure, leading optimization efforts across "
            "microservices teams and implementing standardized deployment "
            "processes for Adobe AEM environments, plus the Splunk "
            "dashboards used to monitor it."
        ),
        "tags": ["Jenkins", "Groovy", "Splunk", "Dynatrace", "Adobe AEM", "JIRA"],
        "achievements": [
            "Cut deployment time by ~90% by automating code deployment pipelines using Jenkins and Groovy scripts.",
            "Reduced production error rates by 60% by spearheading Splunk configuration and log analysis to proactively identify and mitigate errors, issues, and security threats.",
            "Detected potential issues ~90% earlier before reaching production by using Dynatrace to proactively monitor system performance and flag bottlenecks and downtime risks in real time.",
            "Minimized production impact of system changes by conducting comprehensive risk assessments via JIRA change tickets prior to deployment.",
            "Built Splunk dashboards tracking security events, authentication attempts, and access violations, plus performance dashboards for CPU/memory usage and network traffic, improving response times and reducing downtime.",
        ],
        "link": "",
        "link_label": "View project",
        "accent": "#7f9c8c",
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
            "Enabled comprehensive site data collection at scale, as measured by faster crawl completion across large domains, by building a multithreaded crawler bot.",
            "Improved link discovery coverage, as measured by complete extraction of all links from HTML source, by designing a search-tree algorithm.",
            "Increased data accuracy and relevance, as measured by validated canonical tag coverage, by adding canonical tag scraping to the crawler.",
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
        "summary": "Senior Quality Engineer & Site Reliability Engineer based in Santa Ana, CA.",
        "description": (
            "Always exploring how AI agents can make software testing and "
            "infrastructure work smarter. Reach me at "
            "raymondlaurente@gmail.com, or on LinkedIn "
            "(linkedin.com/in/raymond-laurente)."
        ),
        "tags": ["Python", "C++", "C", "Java", "SQL", "Bash/Shell", "Git", "AI-Augmented Testing"],
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
