import os
import json
import sqlite3

def load_to_sqlite(input_dir, db_path):
    """
    Reads transformed JSON files and loads them into an SQLite database.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create tables (use the provided SQL script)
    with open('source/create_tables.sql', 'r') as f:
        cursor.executescript(f.read())

    for file in os.listdir(input_dir):
        with open(os.path.join(input_dir, file), 'r') as f:
            data = json.load(f)

        # Insert into tables
        cursor.execute(
            """
            INSERT INTO jobs (title, industry, description, employment_type, date_posted)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                data["job"]["title"],
                data["job"]["industry"],
                data["job"]["description"],
                data["job"]["employment_type"],
                data["job"]["date_posted"],
            ),
        )

        # Add logic to insert data into other tables (company, education, etc.)

    conn.commit()
    conn.close()
