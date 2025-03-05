CREATE TABLE IF NOT EXISTS reservations (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    chefs_id INT NOT NULL,
    date TIMESTAMP NOT NULL,
    location VARCHAR(255) NOT NULL,
    confirmed_at TIMESTAMP,
    canceled_at TIMESTAMP,
    completed_at TIMESTAMP,
    chefs_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (chefs_id) REFERENCES chefs(id) ON DELETE CASCADE
);
