/*
    Title: final.sql
    Author: Kyle Emory
    Date: 08 July 2022
    Description: final database initilization
*/
DROP USER IF EXISTS 'final_user'@'localhost';
CREATE USER 'final_user'@'localhost'IDENTIFIED WITH mysql_native_password BY 'seasprite';
GRANT ALL PRIVILEGES ON final_database.* TO'final_user'@'localhost';
DROP TABLE IF EXISTS business;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS assets;
DROP TABLE IF EXISTS roles;
-- create the team table 
CREATE TABLE business (
    _revenue     INT             NOT NULL,
    bussiness_name   VARCHAR(75)     NOT NULL,
    _address      VARCHAR(75)     NOT NULL,
    PRIMARY KEY(bussiness_name)
); 

-- create the player table and set the foreign key
CREATE TABLE employee (
    employee_id   INT             NOT NULL        AUTO_INCREMENT,
    first_name  VARCHAR(75)     NOT NULL,
    last_name   VARCHAR(75)     NOT NULL,
    job_code    INT             NOT NULL,
    _salary     INT             NOT NULL,
    PRIMARY KEY(employee_id),
    CONSTRAINT fk_roles 
    FOREIGN KEY(job_code)
        REFERENCES roles(job_code)
);

CREATE TABLE roles (
    job_code   INT             NOT NULL        AUTO_INCREMENT,
    _functions  VARCHAR(75)     NOT NULL,
    _title   VARCHAR(75)     NOT NULL,
    PRIMARY KEY(job_code),
     FOREIGN KEY(employee_id)
        REFERENCES employees(employee_id)
);

CREATE TABLE clients (
    client_id   INT             NOT NULL        AUTO_INCREMENT,
    _name  VARCHAR(75)     NOT NULL,
    _company   VARCHAR(75)     NOT NULL,
    PRIMARY KEY(client_id)
);

CREATE TABLE assets (
    client_id   INT             NOT NULL,
    _name  VARCHAR(75)     NOT NULL,
    _value     INT             NOT NULL,
    PRIMARY KEY(_name), 
    FOREIGN KEY(client_id)
        REFERENCES clients(client_id)
);

CREATE TABLE transactions (
    _value   INT             NOT NULL,
    _name  VARCHAR(75)     NOT NULL,
    _code   INT     NOT NULL    AUTO_INCREMENT,
    client_id     INT             NOT NULL,
    PRIMARY KEY(_code),
    FOREIGN KEY(client_id)
        REFERENCES clients(client_id)
);




-- insert business records
INSERT INTO business(_revenue, business_name,_address)
    VALUES(2000, 'Wizards of the Coast Year 2000', '1100 Walaby way shelby');
INSERT INTO business(_revenue, business_name,_address)
    VALUES(2001, 'Wizards of the Coast Year 2001', '1100 Walaby way shelby');
INSERT INTO business(_revenue, business_name,_address)
    VALUES(2002, 'Wizards of the Coast Year 2002', '1100 Walaby way shelby');
INSERT INTO business(_revenue, business_name,_address)
    VALUES(2003, 'Wizards of the Coast Year 2003', '1100 Walaby way shelby');
INSERT INTO business(_revenue, business_name,_address)
    VALUES(2004, 'Wizards of the Coast Year 2004', '1100 Walaby way shelby');
    INSERT INTO business(_revenue, business_name,_address)
    VALUES(2005, 'Wizards of the Coast Year 2005', '1100 Walaby way shelby');


-- insert employee records 
INSERT INTO employees(employee_id,first_name, last_name, job_code,_salary) 
    VALUES(001,'Bob', 'Burgers',(SELECT job_code FROM roles WHERE _title = 'owner'),30000);
INSERT INTO employees(employee_id,first_name, last_name, job_code,_salary) 
    VALUES(002,'Julius', 'Caesar',(SELECT job_code FROM roles WHERE _title = 'janitor'),400);
INSERT INTO employees(employee_id,first_name, last_name, job_code,_salary) 
    VALUES(003,'Bob', 'Burgers',(SELECT job_code FROM roles WHERE _title = 'secretary'),4000);
INSERT INTO employees(employee_id,first_name, last_name, job_code,_salary) 
    VALUES(004,'Bob', 'Burgers',(SELECT job_code FROM roles WHERE _title = 'accountant'),2000);
INSERT INTO employees(employee_id,first_name, last_name, job_code,_salary) 
    VALUES(005,'Bob', 'Burgers',(SELECT job_code FROM roles WHERE _title = 'support'),2500);
INSERT INTO employees(employee_id,first_name, last_name, job_code,_salary) 
    VALUES(006,'Bob', 'Burgers',(SELECT job_code FROM roles WHERE _title = 'tech'),15000);
 -- insert roles
INSERT INTO roles(_title,_functions)
	VALUES('owner','management');
INSERT INTO roles(_title,_functions)
	VALUES('secretary','record tracking');
 INSERT INTO roles(_title,_functions)
	VALUES('support','customers');
 INSERT INTO roles(_title,_functions)
	VALUES('tech','fix equipment');
 INSERT INTO roles(_title,_functions)
	VALUES('janitor','keep place clean');
 INSERT INTO roles(_title,_functions)
	VALUES('accountant','record for taxes');
-- insert clients
 INSERT INTO clients(_name,_company)
	VALUES('Bill','Tires for All');
 INSERT INTO clients(_name,_company)
	VALUES('Jim','Jims repair shop');
 INSERT INTO clients(_name,_company)
	VALUES('Clyde','Tires for Less');
 INSERT INTO clients(_name,_company)
	VALUES('Jill','Jills Bakery');
 INSERT INTO clients(_name,_company)
	VALUES('Becca','Cars for less');
 INSERT INTO clients(_name,_company)
	VALUES('Julie','Julies Accounting');
-- insert assets
 INSERT INTO assets(client_id,_name,_value)
	VALUES((SELECT client_id FROM clients WHERE _name = 'Jill'),'Raw Goods',1000);
INSERT INTO assets(client_id,_name,_value)
	VALUES((SELECT client_id FROM clients WHERE _name = 'Bill'),'Tires',500);
INSERT INTO assets(client_id,_name,_value)
	VALUES((SELECT client_id FROM clients WHERE _name = 'Julie'),'Liquid Assets',10000);
INSERT INTO assets(client_id,_name,_value)
	VALUES((SELECT client_id FROM clients WHERE _name = 'Becca'),'Cars',40000);
INSERT INTO assets(client_id,_name,_value)
	VALUES((SELECT client_id FROM clients WHERE _name = 'Clyde'),'Tires',2500);
INSERT INTO assets(client_id,_name,_value)
	VALUES((SELECT client_id FROM clients WHERE _name = 'Jim'),'Tools',250);    
    -- insert transactions
 INSERT INTO transactions(client_id,_name,_value,_code)
	VALUES((SELECT client_id FROM clients WHERE _name = 'Jill'),'Accounts Recivable',2000,001);
INSERT INTO assets(client_id,_name,_value)
	VALUES((SELECT client_id FROM clients WHERE _name = 'Bill'),'Accounts Payable',250,002);
INSERT INTO assets(client_id,_name,_value)
	VALUES((SELECT client_id FROM clients WHERE _name = 'Julie'),'Accounts Payable',3000,003);
INSERT INTO assets(client_id,_name,_value)
	VALUES((SELECT client_id FROM clients WHERE _name = 'Becca'),'Accounts Recivable',150,004);
INSERT INTO assets(client_id,_name,_value)
	VALUES((SELECT client_id FROM clients WHERE _name = 'Clyde'),'Accounts Recivable',10000,005);
INSERT INTO assets(client_id,_name,_value)
	VALUES((SELECT client_id FROM clients WHERE _name = 'Jim'),'Accounts Payable',2500,006); 
    