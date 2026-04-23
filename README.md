# QuantEngine 📈

**Risk and Return Calculator — Production Flask Application**

🔗 [Live App](https://quantengine-stp5.onrender.com/)

---

## What is QuantEngine?

QuantEngine is a production web application for running investment risk and return calculations and tracking scenarios over time. Users register an account, input investment parameters, and save results to a personal history they can revisit and compare.

Started as a bootcamp capstone project (Career Tree, March 2026), QuantEngine has since been refactored from a monolithic single-file Flask app into a modular, production-grade application, reviewed by a Principal Engineer, deployed to Render with PostgreSQL, and under active continued development.

---

## Features

- 🔐 **User authentication** — register, log in and log out; all calculation and history pages are protected routes
- 🧮 **Risk and return calculator** — base, optimistic and pessimistic scenario outputs from a single set of inputs
- 🗃️ **Scenario history** — results are persisted per user so you can revisit and compare past calculations
- 🌐 **Production deployment** — live on Render with PostgreSQL, automatic HTTPS, and CI/CD via GitHub

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Database ORM | SQLAlchemy |
| Database | PostgreSQL (production) / SQLite (development) |
| Frontend | HTML, CSS (Jinja2 templates) |
| Auth | Flask-Login, Werkzeug password hashing |
| Testing | pytest |
| Server | Gunicorn |
| Deployment | Render |

---
## Design

| Token | Value | Usage |
|---|---|---|
| Primary Pink | `#f6aeaa` | Buttons, accents, brand colour |
| Teal | `#0d9488` | Header background |
| Background | `#fdfbf9` | Warm off-white page background |
| Success Green | `#10b981` | Low risk indicators |
| Warning Amber | `#f59e0b` | Medium risk indicators |

Responsive design with CSS Grid and Flexbox — layouts adapt from three-column desktop to single-column mobile at 600px breakpoint.
---

## Project Structure

```
quantengine/
├── run.py                      # Application entry point
├── app/
│   ├── __init__.py             # Application factory (create_app)
│   ├── config.py               # Environment-based configuration
│   ├── calculations.py         # Core risk and return logic (separated from routing)
│   ├── models/
│   │   ├── __init__.py         # Public model interface
│   │   ├── user.py             # User model
│   │   └── scenario.py        # Scenario model
│   └── routes/                 # Flask Blueprints
│       ├── auth.py             # Register, login, logout
│       ├── calculate.py        # Calculator route
│       └── history.py         # History and delete routes
├── templates/                  # Jinja2 HTML templates
├── static/                     # CSS and static assets
├── tests/                      # pytest test suite
├── Procfile                    # Render deployment config
├── render.yaml                 # Infrastructure as code (Render)
└── requirements.txt
```

---

## Architecture

QuantEngine v2.0 was a deliberate refactor of the original single-file submission, applying professional Flask patterns throughout:

- **App factory pattern** — `create_app()` in `app/__init__.py` enables environment-specific instances and clean testability
- **Flask Blueprints** — routes split by domain (`auth`, `calculate`, `history`), each self-contained
- **Separated concerns** — config, models, business logic and routing each live in their own modules
- **Single Responsibility** — each model in its own file; calculation logic extracted from routes into `calculations.py`
- **Environment-based config** — secrets and database URLs read from environment variables; no credentials in code

---

## Getting Started

```bash
# Clone the repo
git clone https://github.com/mimimanlyosei/quantengine.git
cd quantengine

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python run.py
```

App runs at `http://localhost:5555`

---

## Deployment

QuantEngine is deployed on Render with a managed PostgreSQL database.

- **Auto-deploy**: pushes to `main` branch trigger automatic redeployment (~2–3 minutes)
- **Environment variables**: `SECRET_KEY` (auto-generated) and `DATABASE_URL` (Render-managed) set via `render.yaml`
- **Database**: SQLAlchemy handles SQLite (local) and PostgreSQL (production) with a single config switch
- **Server**: Gunicorn WSGI server in production (Flask dev server in development only)

---

## Development Process

This project is developed using a structured workflow to simulate professional engineering practice:

- Feature branches with pull requests reviewed and merged by a Principal Engineer
- All tickets tracked on a GitHub Project board, organised into epics
- Incremental, meaningful commits per ticket
- Manual regression testing after each architectural change

---

## Roadmap

| Epic | Status |
|---|---|
| ✅ Code Quality & Architecture | Complete — Blueprints, app factory, modular models |
| ✅ Deployment | Complete — Render, PostgreSQL, CI/CD |
| ✅ UI & UX Polish | Complete — responsive design, card layouts, pink colour scheme |
| ⬜ Testing | Upcoming — pytest unit and route tests |
| ⬜ v3.0 — F.I.R.E. Calculator | Planned |
| ⬜ v4.0 — Monte Carlo & Backtesting | Planned |

---

## Author

**Mimi** — career changer transitioning from Agile delivery into software and data engineering.

[GitHub](https://github.com/mimimanlyosei) · [LinkedIn](https://www.linkedin.com/in/mimimanlyosei)