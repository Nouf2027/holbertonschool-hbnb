-- 1-seed_data.sql
-- Insert initial admin + amenities

USE hbnb;

-- Admin user (fixed id)
INSERT INTO users (id, email, first_name, last_name, password, is_admin)
VALUES (
  '36c9050e-ddd3-4c3b-9731-9f487208bbc1',
  'admin@hbnb.io',
  'Admin',
  'HBnB',
  '$2b$12$uzlPXhXj/prU9tBDXeBkseM38oE1O.ohViVw95o6Ddc5i8VzDq/g2',
  TRUE
);

-- Initial amenities (UUID4 generated)
INSERT INTO amenities (id, name) VALUES
('d5a70a28-5212-40c7-942c-47ed81d6a07a', 'WiFi'),
('1a928a5a-1c28-4a79-8d77-381d0378c133', 'Swimming Pool'),
('55ae27ee-b06f-44ca-9db6-f4f87543d0a0', 'Air Conditioning');
