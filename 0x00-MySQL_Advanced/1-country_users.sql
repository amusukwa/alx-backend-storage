-- Create a table users if it doesn't already exist

CREATE TABLE IF NOT EXISTS users (
    -- Primary key column for unique identification
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),    
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
