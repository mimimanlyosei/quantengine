"""
One-off migration script.
Adds any missing columns to existing tables without dropping data.
Safe to run multiple times - uses IF NOT EXISTS.
"""
from app import create_app, db
from sqlalchemy import text

app = create_app()
with app.app_context():
    with db.engine.connect() as conn:
        conn.execute(text(
            "ALTER TABLE scenario ADD COLUMN IF NOT EXISTS name VARCHAR(100)"
        ))
        conn.commit()
    print("Migration complete.")
