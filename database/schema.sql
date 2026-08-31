CREATE DATABASE IF NOT EXISTS student_result_db;

USE student_result_db;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    roll_number VARCHAR(20) NOT NULL UNIQUE,
    course VARCHAR(100) NOT NULL,

    physics DECIMAL(5,2) NOT NULL,
    chemistry DECIMAL(5,2) NOT NULL,
    mathematics DECIMAL(5,2) NOT NULL,
    english DECIMAL(5,2) NOT NULL,
    computer DECIMAL(5,2) NOT NULL,

    total DECIMAL(6,2) NOT NULL,
    percentage DECIMAL(5,2) NOT NULL,
    grade VARCHAR(5) NOT NULL,
    result VARCHAR(10) NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);
