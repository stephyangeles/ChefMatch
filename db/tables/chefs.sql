CREATE TABLE IF NOT EXISTS chefs (
    id SERIAL PRIMARY KEY,
    specialty_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    bio TEXT,
    FOREIGN KEY (specialty_id) REFERENCES specialty(id) ON DELETE CASCADE
);
