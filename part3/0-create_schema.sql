-- 0-create_schema.sql
-- HBnB schema (raw SQL) - MySQL/InnoDB

DROP DATABASE IF EXISTS hbnb;
CREATE DATABASE IF NOT EXISTS hbnb
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_unicode_ci;

USE hbnb;

-- USER
CREATE TABLE IF NOT EXISTS users (
  id CHAR(36) NOT NULL,
  first_name VARCHAR(255) NOT NULL,
  last_name  VARCHAR(255) NOT NULL,
  email      VARCHAR(255) NOT NULL,
  password   VARCHAR(255) NOT NULL,
  is_admin   BOOLEAN NOT NULL DEFAULT FALSE,
  PRIMARY KEY (id),
  UNIQUE KEY uq_users_email (email)
) ENGINE=InnoDB;

-- PLACE
CREATE TABLE IF NOT EXISTS places (
  id CHAR(36) NOT NULL,
  title VARCHAR(255) NOT NULL,
  description TEXT NULL,
  price DECIMAL(10,2) NOT NULL DEFAULT 0.00,
  latitude FLOAT NULL,
  longitude FLOAT NULL,
  owner_id CHAR(36) NOT NULL,
  PRIMARY KEY (id),
  KEY idx_places_owner_id (owner_id),
  CONSTRAINT fk_places_owner
    FOREIGN KEY (owner_id) REFERENCES users(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE=InnoDB;

-- REVIEW
CREATE TABLE IF NOT EXISTS reviews (
  id CHAR(36) NOT NULL,
  text TEXT NOT NULL,
  rating INT NOT NULL,
  user_id CHAR(36) NOT NULL,
  place_id CHAR(36) NOT NULL,
  PRIMARY KEY (id),
  KEY idx_reviews_user_id (user_id),
  KEY idx_reviews_place_id (place_id),

  -- user can leave only one review per place
  UNIQUE KEY uq_reviews_user_place (user_id, place_id),

  -- rating between 1 and 5
  CONSTRAINT chk_reviews_rating CHECK (rating BETWEEN 1 AND 5),

  CONSTRAINT fk_reviews_user
    FOREIGN KEY (user_id) REFERENCES users(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,

  CONSTRAINT fk_reviews_place
    FOREIGN KEY (place_id) REFERENCES places(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE=InnoDB;

-- AMENITY
CREATE TABLE IF NOT EXISTS amenities (
  id CHAR(36) NOT NULL,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY uq_amenities_name (name)
) ENGINE=InnoDB;

-- PLACE_AMENITY (many-to-many)
CREATE TABLE IF NOT EXISTS place_amenity (
  place_id CHAR(36) NOT NULL,
  amenity_id CHAR(36) NOT NULL,
  PRIMARY KEY (place_id, amenity_id),
  KEY idx_pa_amenity_id (amenity_id),
  CONSTRAINT fk_pa_place
    FOREIGN KEY (place_id) REFERENCES places(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT fk_pa_amenity
    FOREIGN KEY (amenity_id) REFERENCES amenities(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE=InnoDB;
