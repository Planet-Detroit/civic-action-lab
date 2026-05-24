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

## Waitlist form (Formspree)

The waitlist form collects: **Name, Email, Organization, Role**.

It uses [Formspree](https://formspree.io) to handle submissions — no backend needed. Formspree stores all responses in a dashboard and sends email notifications.

### Setup

The form is connected to Formspree form ID `meedlkwr`. Email notifications go to Nina and Ashley.

To change notification recipients, log into [formspree.io](https://formspree.io) and update the form's **Settings > Email Notifications**.

### Viewing responses

All submissions are stored in the Formspree dashboard at [formspree.io/forms](https://formspree.io/forms). You can also export them as CSV from there.

### Formspree free tier limits

- 50 submissions per month
- 2 email recipients
- If you exceed this, Formspree has paid plans starting at $10/month

## Page sections

1. **Hero** — headline + "Get in touch" CTA
2. **The Problem We're Solving** — why civic infrastructure matters
3. **How We Work** — four pillars (built by journalists, tested by publishers, Great Lakes rooted, open-source)
4. **Civic Action Builder** — spotlight on the first tool, with example output box
5. **Who This Is For** — four audience cards
6. **Tools in Development** — pipeline of upcoming tools (Building Now + Designing Next)
7. **Quote** — pull quote from Nina
8. **About** — background on Planet Detroit and the lab
9. **Waitlist** — sign-up form for interested newsrooms
10. **Work With Us** — direct contact CTA + link to planetdetroit.org

## Files

| File | Purpose |
|------|---------|
| `index.html` | The full page |
| `styles.css` | All styles |
| `og-image.png` | Social sharing image (1200x630) |
| `CNAME` | Custom domain config for GitHub Pages |
| `.gitignore` | Ignores `.DS_Store` |

## Making changes

Edit `index.html` and/or `styles.css`, commit, and push to `main`. The site updates automatically.
