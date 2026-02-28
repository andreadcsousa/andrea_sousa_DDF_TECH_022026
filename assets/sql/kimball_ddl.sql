-- DIMENSÕES

CREATE TABLE dim_category (category_id INT PRIMARY KEY, category_name TEXT NOT NULL);

CREATE TABLE dim_product (
  product_id TEXT PRIMARY KEY,
  product_title TEXT NOT NULL,
  category_id INT NOT NULL,
  price NUMERIC,
  list_price NUMERIC,
  price_segment TEXT,
  rating NUMERIC,
  review_count INT,
  has_rating BOOLEAN,
  is_best_seller BOOLEAN,
  image_url TEXT,
  product_url TEXT,
  CONSTRAINT fk_product_category FOREIGN KEY (category_id) REFERENCES dim_category(category_id)
);

CREATE TABLE dim_date (
  date_id INT PRIMARY KEY,
  month_start DATE NOT NULL,
  year INT NOT NULL,
  month_number INT NOT NULL,
  month_name TEXT NOT NULL
);

CREATE TABLE dim_price_segment (price_segment TEXT PRIMARY KEY);

CREATE TABLE dim_popularity_tier (popularity_tier TEXT PRIMARY KEY);

-- FATOS

CREATE TABLE fact_product_snapshot (
  product_id TEXT PRIMARY KEY,
  units_sold_last_month INT,
  weighted_score NUMERIC,
  strategic_score NUMERIC,
  category_rank INT,
  is_top_10_category BOOLEAN,
  CONSTRAINT fk_fps_product FOREIGN KEY (product_id) REFERENCES dim_product(product_id)
);

CREATE TABLE fact_category_monthly (
  date_id INT NOT NULL,
  category_id INT NOT NULL,
  price_segment TEXT NOT NULL,
  popularity_tier TEXT NOT NULL,
  units_sold INT,
  revenue NUMERIC,
  median_price NUMERIC,
  avg_price NUMERIC,
  PRIMARY KEY (date_id, category_id, price_segment, popularity_tier),
  CONSTRAINT fk_fcm_date FOREIGN KEY (date_id) REFERENCES dim_date(date_id),
  CONSTRAINT fk_fcm_category FOREIGN KEY (category_id) REFERENCES dim_category(category_id),
  CONSTRAINT fk_fcm_price_segment FOREIGN KEY (price_segment) REFERENCES dim_price_segment(price_segment),
  CONSTRAINT fk_fcm_pop_tier FOREIGN KEY (popularity_tier) REFERENCES dim_popularity_tier(popularity_tier)
);