/**/
DROP TABLE IF EXISTS raw.amazon_categories;

CREATE TABLE IF NOT EXISTS raw.amazon_categories (
  ingestion_ts TIMESTAMPTZ DEFAULT now(),
  source TEXT DEFAULT 'kaggle',
  payload JSONB
);

ALTER TABLE raw.amazon_categories
  ALTER COLUMN ingestion_ts SET DEFAULT now(),
  ALTER COLUMN ingestion_ts DROP NOT NULL;

ALTER TABLE raw.amazon_categories
  ALTER COLUMN source SET DEFAULT 'kaggle',
  ALTER COLUMN source DROP NOT NULL;

/**/
DROP TABLE IF EXISTS raw.stg_amazon_categories;

CREATE TABLE raw.stg_amazon_categories (
  id INT,
  category_name TEXT
);

INSERT INTO raw.amazon_categories (id, category_name)
SELECT id, category_name
FROM raw.stg_amazon_categories;

SELECT COUNT(*) FROM raw.amazon_categories;
SELECT * FROM raw.amazon_categories LIMIT 5;