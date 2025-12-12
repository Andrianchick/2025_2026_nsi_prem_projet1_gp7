## Purpose

Short, actionable rules to help AI coding agents work productively on this repository (small Python CLI "AKBank" ATM project).

## Big picture

- This is a simple CLI banking simulation. Key scripts are `ketoune.py` (most complete), `main.py` (alternate implementation), `main.ver1.py` (very small prototype) and `mimimoise.py` (utility that reads/writes `clients.json`).
- Data is persisted locally in `clients.json` (no DB or network). The app reads the file at startup and writes with `sauvegarder_clients`.
- Language and UI: prompts, variables and comments are in French. Keep messages and variable names consistent when editing.

## Key files and responsibilities

- `ketoune.py` — full-featured CLI flow: loading/saving clients, authentication, menu, deposit/withdraw with prebuilt bills and history. Use this as the canonical reference for behavior.
- `main.py` — variant with alternate withdraw logic (asks for per-bill counts). Useful to compare behavior and extract `retraits` `details` shape.
- `main.ver1.py` — minimal prototype used for learning; don’t break it but prefer `ketoune.py` when implementing features.
- `mimimoise.py` — small helper that (re)initializes or prints `clients.json`.
- `clients.json` — canonical data file. Keys at top-level are string IDs (e.g. "123"). Each client object contains: `identifiant`, `mot_de_passe`, `solde`, `depots` (list), and `retraits` (list). `retraits` entries sometimes include a `details` dict mapping bill → count.

## Data model examples

Example client (taken from `clients.json`):

```
"123": {
  "identifiant": "Tralalero",
  "mot_de_passe": 1111,
  "solde": 49940,
  "depots": [ {"montant": 845, "date": "14/01/2024"} ],
  "retraits": [ {"montant": 354, "date": "27/03/2024"} ]
}
```

Notes: top-level keys are strings (IDs). Passwords may be numeric in the JSON but are compared as strings in code — preserve that behavior or update both code and fixture consistently.

## How to run & debug locally

- Run the app with: `python ketoune.py` or `python main.py` from the repository root (Windows PowerShell). Both files implement a `main()` entrypoint. `ketoune.py` is the preferred entrypoint for most tasks.
- There are no external dependencies beyond the Python standard library. The codebase appears compatible with Python 3.13 (pycache shows `cpython-313`).
- When testing interactively, consider removing or setting `time.sleep(...)` calls to 0 to speed iterations.

## Project-specific conventions & patterns

- French naming / UI: keep prompts and printed messages in French for consistency.
- Persistence: always use the provided `charger_clients` / `sauvegarder_clients` helpers when reading/writing `clients.json` to preserve formatting (`ensure_ascii=False`, `indent=4`).
- Date format: `"%d/%m/%Y"` (dd/mm/YYYY) — use this format when adding history entries.
- `retraits` entries: may include an optional `details` dict with bill breakdown (see `main.py`). If you change the shape, update both writer and reader code.

## Safe edits & gotchas

- Avoid changing the top-level `clients.json` keys from strings to integers without updating all loader code — authentication iterates `clients.items()` and returns the top-level key.
- Input validation is ad-hoc; when adding stricter validation, keep user-facing error messages in French and ensure flows still call `sauvegarder_clients` when appropriate.
- The code uses blocking `input()` calls for interaction; adding automated tests will require refactoring I/O into injectable functions or using `unittest.mock` to patch `builtins.input`.

## Suggested useful tasks for an AI

- Add type hints and small unit tests for `charger_clients`, `sauvegarder_clients`, and withdraw/deposit logic (refactor to pure functions where possible).
- Improve input validation and consolidate duplicate logic between `ketoune.py` and `main.py` into a shared module.
- Add a small CLI argument to run in "fast" mode (skip sleeps) to speed automated tests.

## Example prompts for the repo maintainer

- "Refactor input/output so I can unit test withdraw logic. Keep French messages; show the new function signatures and a 1–2 test examples using pytest."
- "Add a CLI flag `--no-sleep` that disables `time.sleep` calls for fast execution and testability. Update `ketoune.py` to honor it."

If any part of this file is unclear or you want the agent to follow a tighter rule (naming, tests, or which file is canonical), tell me and I will update the guidance.
