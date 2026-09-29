#!/usr/bin/env bash
# One-time: set your GitHub username everywhere, create the repo, push, tag v1.0.0.
# Usage: bash scripts/publish.sh <github-username>
# Needs: git, and the GitHub CLI (gh) logged in — `brew install gh && gh auth login`
set -euo pipefail
cd "$(dirname "$0")/.."
GH_USER="${1:?Usage: bash scripts/publish.sh <github-username>}"

echo "→ Setting GitHub username to $GH_USER"
grep -rl "YOUR-GITHUB-USERNAME" --exclude-dir=.git --exclude=publish.sh . | while read -r f; do
  if [[ "$(uname)" == "Darwin" ]]; then sed -i '' "s/YOUR-GITHUB-USERNAME/$GH_USER/g" "$f"; else sed -i "s/YOUR-GITHUB-USERNAME/$GH_USER/g" "$f"; fi
done

echo "→ Initialising git"
[ -d .git ] || git init -b main
git add -A
git commit -m "gsc-quick-wins v1.0.0 — first public release" || true

echo "→ Creating public repo and pushing"
gh repo create "$GH_USER/gsc-quick-wins" --public --source=. --push \
  --description "No new articles. More traffic. An Agent Skill that finds your Google Search Console keywords stuck in positions 4–20 and writes the exact fixes." \
  --homepage "https://$GH_USER.github.io/gsc-quick-wins/"

gh repo edit "$GH_USER/gsc-quick-wins" \
  --add-topic claude-skills --add-topic agent-skills --add-topic claude-code \
  --add-topic seo --add-topic google-search-console --add-topic ctr-optimization

echo "→ Turning on GitHub Pages from /docs"
gh api -X POST "repos/$GH_USER/gsc-quick-wins/pages" \
  -f "source[branch]=main" -f "source[path]=/docs" >/dev/null 2>&1 || echo "  (Pages already on, or enable it in Settings → Pages → main /docs)"

echo "→ Tagging v1.0.0 (triggers the release zip)"
git tag -f v1.0.0 && git push -f origin v1.0.0

echo
echo "Done: https://github.com/$GH_USER/gsc-quick-wins"
echo "Site (1–2 min): https://$GH_USER.github.io/gsc-quick-wins/"
