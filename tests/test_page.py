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

# 1. Two waitlist buttons open the Google Form in a new tab: one in the hero,
#    one in the waitlist section. Both carry waitlist-cta so GA logs them as
#    waitlist clicks.
btns = re.findall(r'<a[^>]+href="' + re.escape(GFORM_URL) + r'"[^>]*>', html_src)
check(
    "Two waitlist buttons link to the Google Form",
    len(btns) == 2
    and all(
        "waitlist-cta" in b and 'target="_blank"' in b and 'rel="noopener"' in b
        for b in btns
    ),
    f"found {len(btns)}: {btns}",
)
hero_block = html_src.split('class="hero"')[1].split("<section")[0]
check("Hero contains a waitlist button", "waitlist-cta" in hero_block)

# 2. No embedded iframe — Nina rejected the embed (looked broken); the button
#    is the intended design. This catches an accidental revert.
check("No Google Form iframe on the page", "<iframe" not in html_src)

# 3. Formspree is gone — no action URL, no leftover <form> in the waitlist.
check("No Formspree references remain", "formspree" not in html_src.lower())
check(
    "Old waitlist <form> removed",
    'class="waitlist-form"' not in html_src and 'id="organization"' not in html_src,
)

# 4. The tool is consistently called "Civic Action Toolbox" — the old
#    "Civic Action Builder" name should not appear anywhere on the page.
check(
    'Tool named "Toolbox" everywhere, no "Builder" left',
    "Civic Action Builder" not in html_src and "Civic Action Toolbox" in html_src,
)

# 5. The GA snippet no longer references form fields that don't exist
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
