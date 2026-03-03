/**/
CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS standardized;
CREATE SCHEMA IF NOT EXISTS curated;

/**/
DROP TABLE IF EXISTS raw.amazon_products;

CREATE TABLE IF NOT EXISTS raw.amazon_products (
  ingestion_ts TIMESTAMPTZ DEFAULT now(),
  source TEXT DEFAULT 'kaggle',
  payload JSONB
);

/**/
DROP TABLE IF EXISTS raw.stg_amazon_products;

CREATE TABLE raw.stg_amazon_products (
  asin TEXT,
  title TEXT,
  imgUrl TEXT,
  productURL TEXT,
  stars TEXT,
  reviews TEXT,
  price TEXT,
  listPrice TEXT,
  category_id TEXT,
  isBestSeller TEXT,
  boughtInLastMonth TEXT
);

/**/
SELECT
  asin,
  title,
  REPLACE(price, ',', '.')::NUMERIC(10,2) AS price,
  REPLACE(listPrice, ',', '.')::NUMERIC(10,2) AS list_price,
  REPLACE(stars, ',', '.')::NUMERIC(3,2) AS stars
FROM raw.stg_amazon_products;

/**/
DROP TABLE IF EXISTS raw.amazon_products;

CREATE TABLE raw.amazon_products (
  ingestion_ts TIMESTAMPTZ DEFAULT now(),
  source TEXT DEFAULT 'kaggle',
  asin TEXT,
  title TEXT,
  imgurl TEXT,
  producturl TEXT,
  stars NUMERIC(3,2),
  reviews INT,
  price NUMERIC(10,2),
  listprice NUMERIC(10,2),
  category_id INT,
  isbestseller BOOLEAN,
  boughtinlastmonth INT
);

/**/
INSERT INTO raw.amazon_products (
  asin, title, imgurl, producturl,
  stars, reviews, price, listprice,
  category_id, isbestseller, boughtinlastmonth
)
SELECT
  asin,
  title,
  imgUrl,
  productURL,
  NULLIF(REPLACE(stars, ',', '.'), '')::NUMERIC(3,2),
  NULLIF(reviews, '')::INT,
  NULLIF(REPLACE(price, ',', '.'), '')::NUMERIC(10,2),
  NULLIF(REPLACE(listPrice, ',', '.'), '')::NUMERIC(10,2),
  NULLIF(category_id, '')::INT,
  CASE
    WHEN LOWER(isBestSeller) IN ('true','1','yes') THEN TRUE
    ELSE FALSE
  END,
  NULLIF(boughtInLastMonth, '')::INT
FROM raw.stg_amazon_products;

/**/
SELECT COUNT(*) FROM raw.amazon_products;
SELECT * FROM raw.amazon_products LIMIT 5;

/**/
CREATE INDEX idx_products_category 
ON raw.amazon_products(category_id);

CREATE INDEX idx_products_stars 
ON raw.amazon_products(stars);