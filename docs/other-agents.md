# Using /gsc-quick-wins with other AI agents

Agents like **Cursor**, **Aider**, **ChatGPT custom GPTs** or any LLM with custom instructions don't have native `SKILL.md` discovery. Use one of these:

## Option 1: Paste into custom instructions

Paste the full contents of [`skills/gsc-quick-wins/SKILL.md`](../skills/gsc-quick-wins/SKILL.md) into your agent's custom instructions or system prompt.

## Option 2: Reference as a file path

If your agent loads instructions from a file, point it at:

```
path/to/skills/gsc-quick-wins/SKILL.md
```

## Option 3: Copy the skill folder

```bash
cp -r skills/gsc-quick-wins/ ~/.your-agent/skills/gsc-quick-wins/
```

## Google Antigravity

- **Project-level:** `.agents/skills/gsc-quick-wins/` is already in this repo (symlink).
- **Global:** copy `skills/gsc-quick-wins/` to `~/.gemini/config/skills/gsc-quick-wins/`.

## Running the helper script without an agent

The scorer works on its own:

```bash
python3 skills/gsc-quick-wins/scripts/find_quick_wins.py Queries.csv --top 20
python3 skills/gsc-quick-wins/scripts/find_quick_wins.py Queries.csv --format csv > wins.csv
```

Paste the table into any chat model along with the SKILL.md for the diagnosis and fixes.
