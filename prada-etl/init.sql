CREATE TABLE IF NOT EXISTS stores (
    id SERIAL PRIMARY KEY,
    brand VARCHAR(50),
    country VARCHAR(100),
    city VARCHAR(100),
    address TEXT,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    raw_json JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);