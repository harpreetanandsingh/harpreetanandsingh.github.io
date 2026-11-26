"""Checks the built _site/ against the site spec. Exit 0 = all checks pass."""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / "_site"

PROJECT_SLUGS = [
    "neural-beta", "tail-risk", "default-prediction", "fomc-event-study",
    "kg-qa", "financial-rag", "10k-analyzer",
]
REQUIRED_PAGES = [
    "index.html", "404.html", "projects/index.html", "research/index.html",
    "resume/index.html", "sitemap.xml", "assets/Harpreet_Singh_Anand_Resume.pdf",
    "assets/img/headshot.jpg",
] + [f"projects/{s}/index.html" for s in PROJECT_SLUGS]

# Built HTML must never contain these (case-sensitive unless noted).
FORBIDDEN = [
    (re.compile(r"\(\d{3}\)\s*\d{3}[-\s]\d{4}"), "US phone number"),
    (re.compile(r"\+91[\s\d]{8,}"), "Indian phone number"),
    (re.compile(r"gmail\.com|yahoo\.", re.I), "personal email domain"),
]
# Extra private patterns live in a git-ignored file so they are never published.
_private = Path(__file__).resolve().parent / "private_patterns.txt"
if _private.is_file():
    for _line in _private.read_text(encoding="utf-8").splitlines():
        if _line.strip() and not _line.startswith("#"):
            FORBIDDEN.append((re.compile(_line.strip()), "private pattern"))
else:
    print("WARN: scripts/private_patterns.txt not found; private-string checks skipped")
NAV_LINKS = ["/", "/projects/", "/research/", "/resume/"]
EMAIL = "hanand35@gatech.edu"

failures = []


def fail(msg):
    failures.append(msg)


class Collector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.srcs, self.classes, self.title = [], [], set(), ""
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "class" in a and a["class"]:
            self.classes.update(a["class"].split())
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag in ("img", "script", "link") and (a.get("src") or a.get("href")):
            self.srcs.append(a.get("src") or a.get("href"))
        if tag == "title":
            self._in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


def parse(path):
    c = Collector()
    c.feed(path.read_text(encoding="utf-8"))
    return c


def resolves(url):
    """True if an internal URL maps to a file in _site."""
    url = url.split("#")[0].split("?")[0]
    if not url:
        return True
    target = SITE / url.lstrip("/")
    return target.is_file() or (target / "index.html").is_file()


def main():
    for leaked in ("linkedin_pic.jpeg", "LinkedInprofile.pdf", "resume_harpreet_nov16.pdf", "private_patterns.txt"):
        if (SITE / leaked).exists():
            fail(f"source file published: {leaked}")

    if not SITE.is_dir():
        print("FAIL: _site/ not found; build the site first")
        return 1

    for rel in REQUIRED_PAGES:
        if not (SITE / rel).is_file():
            fail(f"missing page {rel}")

    for html in SITE.rglob("*.html"):
        rel = html.relative_to(SITE)
        text = html.read_text(encoding="utf-8")
        for pattern, why in FORBIDDEN:
            m = pattern.search(text)
            if m:
                fail(f"{rel}: forbidden {why}: {m.group(0)!r}")
        c = parse(html)
        if not c.title.strip():
            fail(f"{rel}: empty <title>")
        for href in NAV_LINKS:
            if href not in c.links:
                fail(f"{rel}: nav link {href} missing")
        for url in c.links + c.srcs:
            if url.startswith("/") and not url.startswith("//") and not resolves(url):
                fail(f"{rel}: broken internal link {url}")

    css = SITE / "assets" / "css" / "main.css"
    if css.is_file():
        for ref in re.findall(r'url\("?([^")]+)"?\)', css.read_text(encoding="utf-8")):
            if not (css.parent / ref).resolve().is_file():
                fail(f"main.css: missing font/asset {ref}")
    if not (SITE / "assets" / "fonts" / "OFL.txt").is_file():
        fail("font license assets/fonts/OFL.txt missing")

    home = SITE / "index.html"
    if home.is_file():
        c = parse(home)
        if f"mailto:{EMAIL}" not in c.links:
            fail("index.html: mailto link to gatech email missing")
        if "/assets/Harpreet_Singh_Anand_Resume.pdf" not in c.links:
            fail("index.html: resume PDF link missing")
        featured = [l for l in c.links if l.startswith("/projects/") and l != "/projects/"]
        if len(set(featured)) < 4:
            fail(f"index.html: expected 4 featured project links, found {len(set(featured))}")

    if home.is_file():
        text = home.read_text(encoding="utf-8")
        hero = re.search(r'<svg[^>]*class="hero-chart"[^>]*>(.*?)</svg>', text, re.S)
        if not hero:
            fail("index.html: hero chart SVG missing")
        elif hero.group(1).count("<path") < 2:
            fail("index.html: hero chart needs empirical and Normal paths")
        if not re.search(r'<img class="headshot" src="/assets/img/headshot\.jpg" alt="Harpreet Singh Anand"', text):
            fail("index.html: headshot with alt text missing")
        if "ticker" not in parse(home).classes:
            fail("index.html: ticker strip missing")

    for listing_page in ("index.html", "projects/index.html"):
        f = SITE / listing_page
        if not f.is_file():
            continue
        cards = re.findall(r'<article class="card">(.*?)</article>', f.read_text(encoding="utf-8"), re.S)
        for card in cards:
            if 'class="card-thumb"' not in card and 'class="card-tile"' not in card:
                fail(f"{listing_page}: card without thumbnail or tile")

    for slug in PROJECT_SLUGS:
        page = SITE / "projects" / slug / "index.html"
        if not page.is_file():
            continue
        c = parse(page)
        if "key-results" not in c.classes:
            fail(f"projects/{slug}: key-results box missing")
        text = page.read_text(encoding="utf-8")
        for heading in ("Question", "Data", "Method", "Findings"):
            if f">{heading}</h2>" not in text:
                fail(f"projects/{slug}: section '{heading}' missing")

    listing = SITE / "projects" / "index.html"
    if listing.is_file():
        c = parse(listing)
        for slug in PROJECT_SLUGS:
            if f"/projects/{slug}/" not in c.links:
                fail(f"projects/index.html: card for {slug} missing")
        if "other-projects" not in c.classes:
            fail("projects/index.html: other-projects list missing")

    research = SITE / "research" / "index.html"
    if research.is_file():
        n = research.read_text(encoding="utf-8").count('class="publication"')
        if n != 4:
            fail(f"research: expected 4 publications, found {n}")

    resume = SITE / "resume" / "index.html"
    if resume.is_file():
        text = resume.read_text(encoding="utf-8")
        for org in ("Commonwealth Bank", "Financial Services Innovation Lab", "Telus", "North Eastern Space"):
            if org not in text:
                fail(f"resume: experience '{org}' missing")
        if "Jul 2024 – Dec 2024" not in text:
            fail("resume: Telus dates must be 'Jul 2024 – Dec 2024'")

    for f in failures:
        print("FAIL:", f)
    print(f"{len(failures)} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
