# PD Civic Action Lab Landing Page

Landing page for the PD Civic Action Lab at **civiclab.planetdetroit.org**.

## What this page does

A single-page marketing site that explains what the Civic Action Lab is, what tools it builds, who it serves, and how to get involved. Includes a waitlist form for newsrooms interested in piloting tools.

## Tech stack

- Static HTML + CSS (no build step, no JavaScript framework)
- Hosted on **GitHub Pages** from this repo (`Planet-Detroit/civic-action-lab`)
- Custom domain via `CNAME` file pointing to `civiclab.planetdetroit.org`
- Google Analytics 4 for tracking (property ID: `G-5QQJ9SVV07`)

## How deployment works

GitHub Pages serves the `main` branch automatically. Any push to `main` triggers a deploy — usually live within a minute or two. There is no build process; the HTML and CSS are served directly.

## Waitlist form (Google Form)

The waitlist is the **"Civic Action Toolbox — Beta Waitlist"** Google Form, embedded in the page as an iframe. It asks for name, email, role, publication details, CMS, coverage area, reporting types, network memberships, and webinar interest.

A "Trouble seeing the form?" link below the embed opens the same form in a new tab, for anyone whose browser blocks embedded Google content.

### Editing the form

Edit questions directly in Google Forms (whoever owns the form in Google Drive). Question changes appear on the site automatically — no code change needed. Only replace the iframe URL in `index.html` if you switch to a *different* form.

### Viewing responses

Open the form in Google Forms and click the **Responses** tab. From there you can link responses to a Google Sheet for sorting and export.

### Analytics note

Because submissions happen inside Google's iframe, Google Analytics on this page cannot count signups — the response count in Google Forms is the source of truth. GA does track clicks on the "open it in a new tab" link.

### History

The waitlist previously used Formspree (form ID `meedlkwr`, 4 fields: Name, Email, Organization, Role). Replaced with the Google Form in August 2026. Old responses remain in the Formspree dashboard at [formspree.io/forms](https://formspree.io/forms).

## Page sections

1. **Hero** — headline + "Get in touch" CTA
2. **The Problem We're Solving** — why civic infrastructure matters
3. **How We Work** — four pillars (built by journalists, tested by publishers, Great Lakes rooted, open-source)
4. **Civic Action Toolbox** — spotlight on the first tool, with example output box
5. **Who This Is For** — four audience cards
6. **Tools in Development** — pipeline of upcoming tools (Building Now + Designing Next)
7. **Quote** — pull quote from Nina
8. **About** — background on Planet Detroit and the lab
9. **Waitlist** — embedded Google Form (Civic Action Toolbox beta waitlist)
10. **Work With Us** — direct contact CTA + link to planetdetroit.org

## Files

| File | Purpose |
|------|---------|
| `index.html` | The full page |
| `styles.css` | All styles |
| `og-image.png` | Social sharing image (1200x630) |
| `CNAME` | Custom domain config for GitHub Pages |
| `tests/test_page.py` | Checks the waitlist embed is wired correctly (`python3 tests/test_page.py`) |
| `.gitignore` | Ignores `.DS_Store` |

## Making changes

Edit `index.html` and/or `styles.css`, commit, and push to `main`. The site updates automatically.
