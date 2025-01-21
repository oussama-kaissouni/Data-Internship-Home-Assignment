CREATE TABLE IF NOT EXISTS jobs (
    title TEXT,
    industry TEXT,
    description TEXT,
    employment_type TEXT,
    date_posted TEXT
);

CREATE TABLE IF NOT EXISTS company (
    name TEXT,
    link TEXT
);

CREATE TABLE IF NOT EXISTS education (
    required_credential TEXT
);

CREATE TABLE IF NOT EXISTS experience (
    months_of_experience INTEGER,
    seniority_level TEXT
);

CREATE TABLE IF NOT EXISTS salary (
    currency TEXT,
    min_value INTEGER,
    max_value INTEGER,
    unit TEXT
);

CREATE TABLE IF NOT EXISTS location (
    country TEXT,
    locality TEXT,
    region TEXT,
    postal_code TEXT,
    street_address TEXT,
    latitude REAL,
    longitude REAL
);
