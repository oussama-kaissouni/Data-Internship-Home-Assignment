import os
import sqlite3
import json
from src.load import load_to_sqlite

def test_load_to_sqlite(tmp_path):
    # Setup
    db_path = tmp_path / "jobs.db"
    input_dir = tmp_path / "transformed"
    input_dir.mkdir()

    # Mock transformed JSON file
    sample_data = {
        "job": {
            "title": "Engineer",
            "industry": "IT",
            "description": "Develop software",
            "employment_type": "Full-time",
            "date_posted": "2023-01-01"
        },
        "company": {
            "name": "Tech Corp",
            "link": "https://linkedin.com/techcorp"
        },
        "education": {
            "required_credential": "Bachelor's Degree"
        },
        "experience": {
            "months_of_experience": 24,
            "seniority_level": "Junior"
        },
        "salary": {
            "currency": "USD",
            "min_value": 50000,
            "max_value": 70000,
            "unit": "year"
        },
        "location": {
            "country": "USA",
            "locality": "San Francisco",
            "region": "CA",
            "postal_code": "94103",
            "street_address": "123 Market St",
            "latitude": 37.7749,
            "longitude": -122.4194
        }
    }

    sample_file = input_dir / "job_0.json"
    with open(sample_file, "w") as f:
        json.dump(sample_data, f)

    # Test
    load_to_sqlite(input_dir, db_path)

    # Verify
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT title, industry FROM jobs")
    result = cursor.fetchone()
    assert result == ("Engineer", "IT")

    conn.close()
