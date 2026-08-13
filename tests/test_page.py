#!/usr/bin/env python3
"""Checks that the waitlist section uses the Google Form (Civic Action Toolbox
Beta Waitlist) as the signup, and that the old Formspree form is fully removed.

Run with:  python3 tests/test_page.py
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

INDEX = Path(__file__).resolve().parent.parent / "index.html"
GFORM_URL = (
    "https://docs.google.com/forms/d/e/"
    "1FAIpQLSe5XGSfHNzg9tgDWIGP4QKfFAFhV_vvY-Gl3NdPk4IQWWqSvQ/viewform"
)

failures = []


def check(name, condition, detail=""):
    if condition:
        print(f"  PASS  {name}")
    else:
        print(f"  FAIL  {name}  {detail}")
        failures.append(name)


html_src = INDEX.read_text()

# 1. The Google Form is embedded in the page as an iframe (embedded=true keeps
#    Google's own chrome minimal inside the frame).
iframe_match = re.search(r'<iframe[^>]+src="([^"]+)"', html_src)
check(
    "Google Form iframe is embedded",
    iframe_match is not None and iframe_match.group(1).startswith(GFORM_URL)
    and "embedded=true" in iframe_match.group(1),
    f"found: {iframe_match.group(1) if iframe_match else 'no iframe'}",
)

# 2. A plain link to the same form exists as a fallback (opens in a new tab)
#    for anyone whose browser blocks the embed.
fallback = re.search(
    r'<a[^>]+href="' + re.escape(GFORM_URL) + r'[^"]*"[^>]+target="_blank"', html_src
) or re.search(
    r'<a[^>]+target="_blank"[^>]+href="' + re.escape(GFORM_URL) + r'[^"]*"', html_src
)
check("Fallback open-in-new-tab link exists", fallback is not None)

# 3. Formspree is gone — no action URL, no leftover <form> in the waitlist.
check("No Formspree references remain", "formspree" not in html_src.lower())
check(
    "Old waitlist <form> removed",
    'class="waitlist-form"' not in html_src and 'id="organization"' not in html_src,
)

# 4. The GA snippet no longer references form fields that don't exist
#    (the old submit handler read #organization and #role).
ga_block = re.search(r"<script>(.*?)</script>", html_src, re.S).group(1)
check(
    "GA snippet has no stale form-field references",
    "#organization" not in ga_block and "#role" not in ga_block,
)

# 5. The page still parses as HTML with balanced tags for the elements we touched.
class TagBalance(HTMLParser):
    def __init__(self):
        super().__init__()
        self.counts = {}

    def handle_starttag(self, tag, attrs):
        if tag in ("div", "section", "iframe", "form"):
            self.counts[tag] = self.counts.get(tag, 0) + 1

    def handle_endtag(self, tag):
        if tag in ("div", "section", "iframe", "form"):
            self.counts[tag] = self.counts.get(tag, 0) - 1


parser = TagBalance()
parser.feed(html_src)
unbalanced = {t: n for t, n in parser.counts.items() if n != 0}
check("div/section/iframe tags are balanced", not unbalanced, str(unbalanced))

print()
if failures:
    print(f"{len(failures)} check(s) failed")
    sys.exit(1)
print("All checks passed")
