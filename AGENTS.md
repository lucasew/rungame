# Project Conventions and Rules

## Operational Directives
- **Centralized Error Reporting:** All expected or unexpected errors must funnel through the centralized error reporting module at `src/error_reporter.py`. You must NEVER leave an empty catch block or call `console.error`/`print` for errors directly at the call site.
- **Mise:** The project tooling relies entirely on `mise` as the task runner. The entrypoint for CI is `mise run ci`.
- **Tool Versioning:** All tools defined in `mise.toml` must be explicitly version-pinned. Never use 'latest' or 'lts'.

## Project Structure
- `src/` -> Contains application logic, domain responsibilities, and the centralized error reporter.
- `src/rungame.py` -> Main script for executing games.
- `src/error_reporter.py` -> Centralized error-reporting function.
- `tests/` -> Contains test modules for unit and integration testing.
- `mise.toml` -> Definition of tools and tasks to manage the development lifecycle.
