CREATE DATABASE IF NOT EXISTS library;
ALTER DATABASE library CHARACTER SET utf8 COLLATE utf8_general_ci;
USE library;

CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(50)
) CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE TABLE books (
    id INT PRIMARY KEY,
    title VARCHAR(100),
    status ENUM('available', 'borrowed')
) CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE TABLE loan_history (
    id INT PRIMARY KEY,
    user_id INT,
    book_id INT,
    borrow_date DATE,
    due_date DATE,
    return_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
) CHARACTER SET utf8 COLLATE utf8_general_ci;

-- テストデータの挿入
INSERT INTO users (id, name, email) VALUES 
(1, 'Daniel Craig', 'daniel@example.com'),
(2, 'Mads Mikkelsen', 'mads@example.com');

INSERT INTO books (id, title, status) VALUES 
(1, 'Attack on Titan', 'available'),
(2, 'JoJo', 'borrowed');

INSERT INTO loan_history (id, user_id, book_id, borrow_date, due_date, return_date) VALUES 
(1, 1, 2, '2023-06-01', '2023-06-08', NULL);
