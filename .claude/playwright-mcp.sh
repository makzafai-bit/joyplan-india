#!/bin/sh
# Starts the Playwright MCP server (headless) for Claude Code.
# In Claude cloud sessions, use the Chromium that is pre-installed there.
# Anywhere else, Playwright uses its own browser (install with: npx @playwright/mcp@0.0.85 install-browser chrome-for-testing).
set -e
if [ -x /opt/pw-browsers/chromium ]; then
  exec npx -y @playwright/mcp@0.0.85 --headless --isolated --output-dir .playwright-mcp \
    --executable-path /opt/pw-browsers/chromium --no-sandbox "$@"
fi
exec npx -y @playwright/mcp@0.0.85 --headless --isolated --output-dir .playwright-mcp "$@"
