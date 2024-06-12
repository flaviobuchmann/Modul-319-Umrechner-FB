--Execute this File to Create the Database and the Users--
DROP DATABASE IF EXISTS login_system_umrechner;

CREATE DATABASE login_system_umrechner;

USE login_system_umrechner;

-- Tabelle für Benutzerkonten
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(255) DEFAULT 'user',
    -- Speichere verschlüsselte Passwörter, niemals im Klartext!
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabelle für Benutzerdetails
CREATE TABLE user_details (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    name VARCHAR(255) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Tabelle für Login-Versuche (optional, für Sicherheitszwecke)
CREATE TABLE login_attempts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    attempt_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    success TINYINT(1),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Verify the structure of the updated table
DESCRIBE users;