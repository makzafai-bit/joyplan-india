# JoyPlan India website: notes for Claude

The India site must look identical to joyplan.com. Match its layout, fonts, colours, spacing and copy;
do not invent a new look.

## Skills and tools in this repo

- `.claude/skills/frontend-design` (Anthropic) and `.claude/skills/design-taste-frontend` (taste-skill 2.5.1,
  MIT, github.com/Leonxlnx/taste-skill). Both are written for designing new, distinctive sites. Here, use them
  for build quality only: responsive layout, typography, spacing, copy that does not read as AI-made, and
  catching broken visuals. Do not use them to restyle the site, deal a new art direction, swap in stock photos or
  add effects unless the user asks for a redesign.
- Playwright MCP (`.mcp.json`, headless). Use it to check pages in a real browser at 390px and 1440px before
  calling a change done. Serve the folder first (`python3 -m http.server`), since `file://` URLs are blocked.

## Deploy

`main` is deployed to Hostinger `public_html` by webhook, so work on a branch and open a pull request.
`.htaccess` keeps `.claude/`, `.mcp.json`, `.git/` and this file from being served.
