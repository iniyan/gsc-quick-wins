# Contributing

Thanks for helping make /gsc-quick-wins better.

## Good contributions

- **Better CTR benchmarks** — with a source (industry study, your own anonymised data across many sites).
- **New export formats** — Looker Studio, Bing Webmaster Tools, Ahrefs/Semrush GSC connectors. Add the column names to `ALIASES` in `scripts/find_quick_wins.py`.
- **Diagnosis patterns** — new reasons pages get stuck, with the fix.
- **Language/market notes** — e.g. regional-language publishers, news vs. evergreen sites.

## Rules

- Keep the helper script **standard-library only**. No `pip install`.
- Never commit real client or site data. Anonymise or invent example rows.
- Keep `SKILL.md` specific and actionable — "add an H2 titled X", not "improve content".
- Test before opening a PR:

```bash
python3 skills/gsc-quick-wins/scripts/find_quick_wins.py examples/sample-Queries.csv
```

## Versioning

Bump `version` in `.claude-plugin/plugin.json` and add a line to `CHANGELOG.md`.
