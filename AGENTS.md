# Agents Operational Guidelines

This file serves as the core operational manual and project conventions reference for all LLM agents interacting with this repository.

## Important Directives

- **Mise First:** `mise` is the primary task runner for all actions. Before performing any tasks, ensure `mise` is installed. All tasks must be executed via `mise` (e.g., `mise run lint`).
- **Tool Pinning:** Always pin tools installed via `mise.toml`. Do not use `latest` or `lts`.
- **Centralized Error Reporting:** Avoid scattering `console.error` (or `print` in Python). Errors should ideally be funneled to a centralized reporting mechanism to ensure visibility. Wait for an established logger/reporter to be developed, or use robust try/except logic handling context appropriately. Currently, `rungame.py` outputs a basic list of commands on `IndexError`.
- **Python Unit Tests:** Run standard tests via `python3 -m unittest discover tests`.
- **Linting:** Use `mise run lint` (or `workspaced codebase lint` if implemented).

## Codebase Map

- `/rungame.py` -> Main script that launches games based on command-line arguments.
- `/rungame.cmd` -> Windows batch file wrapper for `rungame.py`.
- `/README.md` -> Brief project overview.
