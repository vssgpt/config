# Sweet Sticks

A pack of sweet sticks for each person on the team. Flick a pack open, pull a stick, and it unrolls into that person's visiting card.

Live: https://vssgpt.github.io/config/

## Routes (for QR codes)

| Person | Link |
|---|---|
| Everyone | /config/all/ |
| Vishesh | /config/vishesh/ |
| Kashish | /config/kashish/ (or /kbhumbri/) |
| Atharva | /config/atharva/ (or /athvkd/) |
| Sameen | /config/sameen/ (or /sam/) |
| Eemon | /config/eemon/ |
| Deepika | /config/deepika/ |
| Arjun | /config/arjun/ |
| Mohak | /config/mohak/ |
| Parinishtha | /config/parinishtha/ (or /pari/) |

Every route folder holds the same `index.html`; the page reads the last part of the URL to pick the pack. `#slug` links (e.g. `/config/#sameen`) work too.

Built on vssgpt.

## Editing

`sweet-sticks.html` is the source. After changing it, run `python3 build.py` to refresh `index.html`, `404.html` and the route folders, then push. `.github/workflows/pages.yml` deploys every push to `main`.

## Vercel

The repo is also ready for Vercel: import `vssgpt/config` at vercel.com/new, keep Framework Preset on "Other" with no build command, and deploy. Every push to `main` then redeploys both Vercel and GitHub Pages. On Vercel the links drop the `/config` part, e.g. `your-project.vercel.app/sameen`. `vercel.json` sends any unknown path to the main page, which opens Vishesh's pack.
