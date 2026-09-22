# Create Instructions

- Create new instruction files in `./instructions/` using the `[name].agent.md` naming pattern.
- Use verb-first names with hyphen separators, e.g. `create-report.agent.md`.
- Keep each instruction focused on one workflow or responsibility.
- Write instructions as short, actionable Markdown bullet points.
- Avoid long explanations and preserve a practical, implementation-first tone.
- Add a new catalog entry to `./instructions/main.agent.md` with a one-line description and optional metadata.
- Include `Keywords`, `Target`, and `Exceptions` when they help match the instruction to user requests.
- Prefer small, reusable instructions over large monolithic files.
- When updating an instruction, read the existing file first and make a targeted edit rather than rewriting it wholesale.
- If the repo has no instruction infrastructure yet, install the standard entry-point files for the active IDE.
- For VS Code + Copilot, create or update `.github/copilot-instructions.md` and `.github/prompts/` wrappers as needed.
- For Cursor, create or update `.cursor/rules/` wrappers and ensure the main rules file references `./instructions/main.agent.md`.
- For Claude Code, create or update `.claude/CLAUDE.md` and `.claude/commands/` wrappers as needed.
- Keep instruction content platform-agnostic and reusable across IDEs.
- If a workflow becomes complex, split it into a dedicated instruction or skill instead of expanding one file indefinitely.
- Validate the setup after changes by checking that the catalog and entry-point files exist and reference the correct instruction paths.
