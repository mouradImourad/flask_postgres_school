DROP TABLE IF EXISTS students CASCADE ;
DROP TABLE IF EXISTS teachers CASCADE ;
DROP TABLE IF EXISTS subjects CASCADE ;

CREATE TABLE subjects (
    subject_id SERIAL PRIMARY KEY,
    subject_name VARCHAR (100) NOT NULL
);

CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR (50) NOT NULL,
    last_name VARCHAR (50) NOT NULL,
    age INT,
    subject_id INT,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id) 
);

CREATE TABLE teachers (
    teacher_id SERIAL PRIMARY KEY,
    first_name VARCHAR (50) NOT NULL,
    last_name VARCHAR (50) NOT NULL,
    age INT,
    subject_id INT,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);


INSERT INTO subjects(subject_name) VALUES
('Math'),
('Science'),
('History'),
('Literature'),
('Physical Education');

INSERT INTO students(first_name, last_name, age, subject_id) VALUES
('David', 'Miller', 32, 3),
('Sarah', 'Johnson', 28, 1),
('Robert', 'Williams', 35, 4),
('Emily', 'Anderson', 30, 5),
('Michael', 'Smith', 29, 4),
('Olivia', 'Johnson', 31, 5),
('Matthew', 'Brown', 27, 3),
('John', 'Doe', 29, 1),
('Laura', 'Clark', 30, 2),
('Rebecca', 'Wilson', 33, 2),
('Chris', 'Evans', 31, 1),
('Anna', 'Robinson', 29, 1),
('James', 'Moore', 34, 5),
('Elizabeth', 'White', 28, 3),
('William', 'Harris', 30, 5),
('Julia', 'Lewis', 32, 4),
('Daniel', 'Turner', 29, 3),
('Grace', 'Parker', 35, 4),
('Charles', 'Bennett', 28, 2),
('Sophia', 'Wright', 30, 1);

INSERT INTO teachers(first_name, last_name, age, subject_id) VALUES
('David', 'Miller', 32, 3),
('Sarah', 'Johnson', 28, 1),
('Robert', 'Williams', 35, 4),
('Emily', 'Anderson', 30, 5),
('Michael', 'Smith', 29, 4),
('Olivia', 'Johnson', 31, 5),
('Matthew', 'Brown', 27, 3),
('John', 'Doe', 29, 1),
('Laura', 'Clark', 30, 2),
('Rebecca', 'Wilson', 33, 2),
('Chris', 'Evans', 31, 1),
('Anna', 'Robinson', 29, 1),
('James', 'Moore', 34, 5),
('Elizabeth', 'White', 28, 3),
('William', 'Harris', 30, 5),
('Julia', 'Lewis', 32, 4),
('Daniel', 'Turner', 29, 3),
('Grace', 'Parker', 35, 4),
('Charles', 'Bennett', 28, 2),
('Sophia', 'Wright', 30, 1);




