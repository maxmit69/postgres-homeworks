-- SQL-команды для создания таблиц

CREATE TABLE customers
(
	customer_id VARCHAR PRIMARY KEY,
	company_name VARCHAR(100),
	contact_name VARCHAR(100)
);


CREATE TABLE employees
(
	employee_id INTEGER PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	title VARCHAR(100),
	birth_date DATE,
	notes TEXT
);


CREATE TABLE orders
(
	orders_id SERIAL PRIMARY KEY,
	customer_id VARCHAR(100) REFERENCES customers(customer_id),
	employee_id INTEGER REFERENCES employees(employee_id),
	order_date DATE,
	ship_city VARCHAR(100)
);

