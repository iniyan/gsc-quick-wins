# Publishing checklist (maintainer notes)

## One command

```bash
bash scripts/publish.sh <your-github-username>
```

This replaces `iniyan` in every file, creates the public repo, pushes, adds topics, turns on GitHub Pages from `/docs`, and tags `v1.0.0` — which makes the Release workflow attach `gsc-quick-wins.zip` for Claude.ai users.

Prerequisites: `git`, and the GitHub CLI logged in (`brew install gh && gh auth login`).

## After it's live

- [ ] Check the Actions tab — CI and Release should both be green.
- [ ] Test the install yourself: `npx skills add https://github.com/<you>/gsc-quick-wins --skill gsc-quick-wins`
- [ ] Test the Claude Code plugin: `/plugin marketplace add <you>/gsc-quick-wins`
- [ ] Upload `gsc-quick-wins.zip` from the release into Claude.ai and run it on a real export.
- [ ] Add a social preview image: Settings → General → Social preview (1280×640). A screenshot of the landing-page hero works.
- [ ] It should appear on skills.sh automatically after the first `npx skills add` installs.

## Sharing

- [ ] Post the landing page + a before/after table from a real (anonymised) site.
- [ ] Submit to the Anthropic skills community lists and awesome-claude-skills style repos via PR.
- [ ] List it on Capafy alongside your other skills.

## Releasing an update

1. Edit `skills/gsc-quick-wins/SKILL.md` or the script.
2. Bump `version` in `.claude-plugin/plugin.json`, add a line to `CHANGELOG.md`.
3. `git commit -am "…" && git tag v1.1.0 && git push && git push --tags`
