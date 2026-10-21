CREATE TABLE department(
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL
);



-- ### DDL data defination language it basically means that we are defining the structure and CRUD operations
INSERT INTO department(department_name)
VALUES
('Sales'),
('Support'),
('Warehouse');

select * from department;





CREATE TABLE employees(
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    phone VARCHAR(20),
    bio TEXT,
    job_title VARCHAR(50) NOT NULL,
    salary INT NOT NULL CHECK (salary > 0),
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    hire_date DATE NOT NULL,
    last_login TIMESTAMP,
    employee_status VARCHAR(20) NOT NULL DEFAULT 'active',-- active, on_leave , terminated
                    check (employee_status IN ('active', 'on_leave', 'terminated')),
    created_at TIMESTAMP NOT NULL DEFAULT now(),
    department_id INT REFERENCES department(department_id), -- foreign key realt^n
    manager_id INT REFERENCES employees(employee_id)
);

INSERT INTO employees (first_name, last_name, email, job_title, salary, hire_date, manager_id) 
VALUES ('Dipali', 'Nirala', 'dipalnirala@gmail.com', 'CEO', 200000, '2023-01-01', NULL);

SELECT employee_id
FROM employees
WHERE employee_id = manager_id;

INSERT INTO employees (first_name, last_name, email, department_id, job_title, salary,  hire_date)
VALUES
    ('Priya',  'Nair',      'priya.nair@techbazaar.com',      1, 'Sales Representative', 62000.00, '2020-06-15'),
    ('Fake',   'Robert',    'robert.chen@techbazaar.com',     1, 'Rep',                  50000.00, '2024-01-01'),
    ('Marcus', 'Webb',      'marcus.webb@techbazaar.com',     1, 'Sales Representative', 58000.00, '2021-09-01'),
    ('Elena',  'Garcia',    'elena.garcia@techbazaar.com',    1, 'Senior Sales Rep',     68000.00, '2019-11-20'),
    ('James',  'Okafor',    'james.okafor@techbazaar.com',    2, 'Support Lead',         72000.00, '2018-05-10'),
    ('Lily',   'Zhang',     'lily.zhang@techbazaar.com',      2, 'Support Agent',        48000.00, '2022-02-14'),
    ('Diego',  'Fernandez', 'diego.fernandez@techbazaar.com', 2, 'Support Agent',        46000.00, '2023-01-09'),
    ('Sara',   'Osei',      'sara.osei@techbazaar.com',       3, 'Warehouse Lead',       55000.00, '2020-08-23');


select * from employees;

INSERT INTO employees (first_name, last_name, email, department_id, job_title, salary, hire_date)
VALUES (NULL, 'NoFirstName', 'nofirstname.demo@example.com', 1, 'Rep', 50000.00, '2024-01-01');

INSERT INTO employees (first_name, last_name, email, department_id, job_title, salary, hire_date)
VALUES ('Fake', 'Robert', 'robert.chen@techbazaar.com', 1, 'Rep', 50000.00, '2024-01-01');

INSERT INTO employees (first_name, last_name, email, department_id, job_title, salary, hire_date)
VALUES ('Unpaid', 'Intern', 'unpaid.demo@example.com', 1, 'Intern', 0, '2024-01-01');

INSERT INTO employees (first_name, last_name, email, department_id, job_title, salary, hire_date, employee_status)
VALUES ('Bad', 'Status', 'badstatus.demo@example.com', 1, 'Rep', 50000.00, '2024-01-01', 'retired');

ALTER TABLE employees
ADD COLUMN internal_note varchar(100) NOT NULL DEFAULT 'N/A';
select * from employees;

ALTER TABLE employees
RENAME column internal_note to hr_note;

select * from employees;

ALTER TABLE employees
DROP column hr_note;