#2

DELIMITER $$
CREATE PROCEDURE average()
BEGIN
SELECT AVG(salary)
FROM t_salaries
LIMIT 1000;
END$$
DELIMITER ;
CALL average();

#3 Create a procedure called ‘emp_info’ 
#that uses as parameters the first and the last name of an individual, and returns their employee number.

DELIMITER $$
CREATE PROCEDURE emp_info(first_names text,last_names text)
BEGIN
SELECT emp_no
FROM t_employees
WHERE first_name = first_names and last_name =last_names;
END$$  
DELIMITER ; 

#4
CALL emp_info('Patricio','Bridgland');

#5Create a function called ‘emp_info’ that takes for parameters the first and last name 
#of an employee, and returns the salary from the newest contract of that employee. 
#Hint: In the BEGIN-END block of this program, you need to declare 
#and use two variables – v_max_from_date that will be of the DATE type, and v_salary, that will be of the DECIMAL (10,2) type.

DELIMITER $$
CREATE PROCEDURE emp_info5(first_names text,last_names text)
BEGIN
DECLARE v_max_from_date DATE;
SELECT salary,from_date,to_date
FROM t_salaries
JOIN t_employees
ON t_salaries.emp_no=t_employees.emp_no
WHERE first_name = first_names and last_name =last_names
ORDER BY from_date DESC
LIMIT 1;
END$$  
DELIMITER ; 


CALL emp_info5('Patricio','Bridgland');


#6 Create a trigger that checks if the hire date of an employee is higher than the current date. 
#If true, set this date to be the current date. Format the output appropriately (YY-MM-DD)
DROP TRIGGER hiredayempose
DELIMITER $$
CREATE TRIGGER hiredayempose
BEFORE UPDATE ON t_employees
FOR EACH ROW
BEGIN
	IF NEW.hire_date > CURDATE() THEN 
		SET NEW.hire_date = date_format(CURDATE(), '%Y-%m-%d'); 
	END IF; 
END $$
DELIMITER ;


INSERT INTO t_employees VALUES ('1049914', '2020-12-02','Patricios','Bridglandas','F','2030-12-02');
SELECT * FROM t_employees
WHERE last_name='Bridglandas';

#8Select all records from the ‘salaries’ table of people whose salary is higher than $89,000 per annum. 
#Then, create an index on the ‘salary’ 
#column of that table, and check if it has sped up the search of the same SELECT statement.
CREATE INDEX indexe ON t_salaries (salary);

SELECT * 
FROM t_salaries
WHERE salary>89000;

#9 Use Case statement and obtain a result set containing the employee number, 
#first name, and last name of all employees with a number higher than 109990. 
#Create a fourth column in the query, indicating whether this employee is also a manager, 
#according to the data provided in the dept_manager table, or a regular employee.

ALTER TABLE t_employees 
ADD COLUMN managerornot char(50);

SELECT t_employees.emp_no,t_employees.first_name,t_employees.last_name,managerornot,
CASE
    WHEN t_dept_manager.emp_no=t_employees.emp_no THEN "Manager"
    ELSE "employee"
END
FROM t_employees
INNER JOIN t_dept_manager
ON t_dept_manager.emp_no=t_employees.emp_no
WHERE t_employees.emp_no>'109990';


#Extract a dataset containing the following information about the managers: employee number, first name, and last name. 
#Add two columns at the end – one showing the difference between the maximum and minimum salary of that employee, 
#and another one saying whether this salary raise was higher than $30,000 or NOT.

CREATE TEMPORARY TABLE ana
SELECT salary,t_salaries.from_date,t_salaries.to_date,t_dept_manager.emp_no,first_name,last_name
FROM t_employees
INNER JOIN t_dept_manager
ON t_dept_manager.emp_no=t_employees.emp_no
INNER JOIN t_salaries
ON t_salaries.emp_no=t_employees.emp_no;

select *
from anados;

CREATE TEMPORARY TABLE anados
SELECT first_name,last_name,max(salary)-min(salary) as diff
FROM ana
GROUP BY first_name,last_name;

SELECT first_name,last_name,diff,
CASE
    WHEN diff>30000 THEN "higher"
    ELSE "lower"
END AS higher30k
FROM anados;

#10 Extract the employee number, first name, and last name of the first 100 employees,
# and add a fourth column, called “current_employee” saying “Is still employed” 
#if the employee is still working in the company, or “Not an employee anymore”
# if they aren’t. Hint: You’ll need to use data from both the ‘employees’ and the ‘dept_emp’ table to solve this exercise.

SELECT t_employees.emp_no,t_employees.first_name,t_employees.last_name,t_dept_emp.to_date,
CASE
   WHEN t_dept_emp.to_date<"2021-01-21" THEN "Not working"
   ELSE "Still Working"
END AS Workingornot
FROM t_employees
INNER JOIN t_dept_emp
ON t_employees.emp_no=t_dept_emp.emp_no
LIMIT 100