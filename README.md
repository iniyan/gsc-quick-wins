# /gsc-quick-wins

**No new articles. More traffic.**

`/gsc-quick-wins` is an Agent Skill that turns your Google Search Console export into a prioritised fix list for pages Google *already* ranks — the keywords stuck in positions 4–20 — and writes the exact titles, H2s, FAQs and internal links to push them onto page one.

> Moving a keyword from #8 to #3 is often worth more traffic than publishing ten new articles. The easiest SEO wins are hiding between positions 4 and 20.

Works with Claude Code, Claude.ai, Codex CLI, opencode, Google Antigravity, Cursor and any agent that reads `SKILL.md`.

---

## Install

**Claude Code (plugin marketplace)**

```
/plugin marketplace add iniyan/gsc-quick-wins
/plugin install gsc-quick-wins@gsc-quick-wins
```

**Any other agent** — one command via the [`skills`](https://github.com/vercel-labs/skills) CLI (Cursor, Codex, Copilot, Gemini CLI, opencode, and more):

```
npx skills add https://github.com/iniyan/gsc-quick-wins --skill gsc-quick-wins
```

Add `-g` to install globally (every project); drop it to scope to the current one.

**Claude.ai / Claude desktop app**

Download [`gsc-quick-wins.zip`](https://github.com/iniyan/gsc-quick-wins/releases/latest) from Releases, then go to **Settings → Capabilities → Skills → Upload skill**.

**No installer? Copy it directly.**

```
git clone https://github.com/iniyan/gsc-quick-wins.git
rsync -a --exclude '.DS_Store' gsc-quick-wins/skills/gsc-quick-wins/ ~/.claude/skills/gsc-quick-wins/
```

Restart Claude Code after copying.

### Also works with

This repo exposes the skill at every agent's standard discovery path via symlinks. No extra config needed.

| Agent | How it discovers |
|---|---|
| **Claude Code** | `.claude/skills/gsc-quick-wins/` (plus the `.claude-plugin/` marketplace install above) |
| **Codex CLI** | `.agents/skills/gsc-quick-wins/`, walking up to repo root |
| **opencode** | `.opencode/skills/gsc-quick-wins/` at project root |
| **Google Antigravity** | `.agents/skills/gsc-quick-wins/` or `~/.gemini/config/skills/gsc-quick-wins/` globally |
| **Other agents** | Point custom instructions at `skills/gsc-quick-wins/SKILL.md` — see [`docs/other-agents.md`](docs/other-agents.md) |

> **Windows users:** clone with `git clone -c core.symlinks=true` and enable Developer Mode. If symlinks don't work, copy `skills/gsc-quick-wins/` into your agent's skill folder instead.

---

## Use it

**1. Export your data from Search Console**

Performance → Search results → Date: *Last 3 months* → **Export → Download CSV**. Unzip it — you want `Queries.csv` (and `Pages.csv` if you want query-to-URL mapping).

**2. Hand it to your agent**

```
/gsc-quick-wins — here's my Queries.csv. Find my quick wins.
```

Or just talk normally — the skill triggers on things like:

- "Why is my page stuck at position 8?"
- "CTR is low on GSC, what do I fix?"
- "I don't want to write new content but I want more traffic."
- "Optimise this page — it ranks #11 for *marathon training plan*."

**3. What you get back**

- A **priority table** — keyword, page, position, impressions, CTR vs. expected CTR, the likely issue and the fix.
- A **diagnosis** per page — content gap, CTR problem, or authority (internal link) problem.
- A **ready-to-paste action plan** — rewritten title tag and meta description, the exact H2 to add, 3–5 FAQ questions, schema to add, internal links with anchor text.
- A **do-first / do-second / skip** order so you know where to start on Monday.

### Example

Running the bundled helper on [`examples/sample-Queries.csv`](examples/sample-Queries.csv):

```
python3 skills/gsc-quick-wins/scripts/find_quick_wins.py examples/sample-Queries.csv --top 5
```

| Keyword | Pos | Impr. | CTR | Exp. CTR | +Clicks @#3 | Tier | Issue | Action |
|---|---|---|---|---|---|---|---|---|
| how to clean white sneakers | 5.3 | 12,400 | 0.77% | 7.5% | 1,330 | Do first | Low CTR for position | Rewrite title + meta description |
| marathon training plan for beginners | 11.4 | 15,600 | 0.77% | 1.5% | 1,674 | Do first | Content gap + low CTR | Add dedicated section, fix title |
| running shoes vs walking shoes | 7.8 | 8,900 | 3.48% | 3.5% | 713 | Do first | Content gap | Add dedicated section answering the query |
| how long do running shoes last | 13.7 | 6,100 | 1.44% | 1.5% | 613 | Do second | Thin topical depth | Expand content + add internal links |
| trail running shoes waterproof | 9.2 | 3,900 | 1.15% | 3.5% | 403 | Do first | Content gap + low CTR | Add dedicated section, fix title |

The agent then takes this table and writes the actual fixes. See [`examples/sample-output.md`](examples/sample-output.md) for a full run.

---

## How it works

```
GSC export
  ↓ keep positions 4–20   (1–3 already win, 21+ is too far to move quickly)
  ↓ sort by impressions   (volume = opportunity)
  ↓ compare CTR to the benchmark for that position
For each priority keyword:
  → content gap?   add a dedicated H2, adjacent questions, entities, FAQ
  → CTR gap?       rewrite title + meta, add schema for rich results
  → authority gap? add internal links with keyword-rich anchors
  → re-submit URL in GSC, re-check in 2–4 weeks
```

The skill owns the strategy and the writing. The optional helper script (`scripts/find_quick_wins.py`, Python 3.8+, standard library only) does the number-crunching so large exports are scored exactly instead of eyeballed.

## Requirements

- An agent that supports Agent Skills (see the table above), or any LLM with custom instructions
- A Google Search Console property with data (3 months recommended)
- *Optional:* Python 3.8+ to run the helper script — no `pip install` needed

## What's in this repo

- `skills/gsc-quick-wins/SKILL.md` — the skill
- `skills/gsc-quick-wins/scripts/find_quick_wins.py` — zero-dependency CSV scorer
- `examples/` — a sample GSC export and a full sample output
- `docs/` — landing page (GitHub Pages) and guide for other agents
- `.claude-plugin/` — plugin manifest + marketplace catalog
- `.claude/skills/`, `.agents/skills/`, `.opencode/skills/` — symlinks → `skills/gsc-quick-wins/`

## Privacy

Your GSC export never leaves your machine unless your agent sends it to its model. The helper script makes no network calls. Don't commit real client exports — `.gitignore` blocks `*.private.csv` and `gsc-exports/` by default.

## Contributing

Ideas, bug reports and better CTR benchmarks are welcome — open an issue or a PR. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Author

Built by [Thamiziniyan](https://iniyan.in) at [Cubbing Solutions](https://cubbingsolutions.com) — a decade of growing traffic for Tamil and Indian digital publishers, packaged as a skill.

MIT licensed.
