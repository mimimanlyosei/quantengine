# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

**Run the app:**
```bash
python run.py
```
Runs on `http://127.0.0.1:5555` in debug mode.

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Database setup** (first run or after model changes):
```bash
python -c "from app import create_app, db; app = create_app(); app.app_context().push(); db.create_all()"
```

**Check DB health:** `GET /health/db` returns `{"db": "ok"}`.

No test runner or linter is configured yet.

## Architecture

QuantEngine is a Flask investment calculator app. Users register, input parameters, and receive three compound-interest projections (base, optimistic, pessimistic).

**Application factory** lives in `app/__init__.py` (`create_app()`). It registers three Blueprints and initialises SQLAlchemy + Flask-Login. `run.py` is the entry point; `app.py` is a legacy duplicate that should eventually be removed.

**Blueprints** (`app/routes/`):
- `auth` — register / login / logout
- `calculate` — investment form, calls `calculations.py`, saves a `Scenario`
- `history` — list and delete saved scenarios

**Core logic** (`app/calculations.py`): `calculate_scenarios(initial_investment, expected_return, years)` applies compound interest at base rate and ±5% swing to produce three results. All monetary inputs are in GBP (£).

**Models** (`app/models/`):
- `User` — Flask-Login UserMixin, stores `password_hash` (Werkzeug)
- `Scenario` — stores inputs + three result values; `validate()` checks ranges before saving (investment £1–£999,999,999; return 0–50%; years 1–70; risk_appetite low/medium/high)

**Templates** (`templates/`) use a shared `base.html` with navigation and flash messages. No frontend build step — plain CSS/JS in `static/`.

**Config** (`app/config.py`): hardcoded `SECRET_KEY` and SQLite path (`instance/app.db`). Production deployment needs real environment variables.

## Roadmap context

The `docs/planning/MATH_LEARNING_ROADMAP.md` ties planned features to the owner's maths learning path:
- v3.0: F.I.R.E. calculator, inflation adjuster, break-even calculator
- v4.0+: Monte Carlo simulation, risk metrics, historical backtesting (after probability/statistics courses)

New features should be added as additional Blueprints following the existing pattern.
