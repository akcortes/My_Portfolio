## Tableau and SQL Connenction 

# Result - Dashboard in Tableau

https://prod-uk-a.online.tableau.com/#/site/anaka/workbooks/98402?:origin=card_share_link

# SQL script

#1

SELECT 
YEAR(d.from_date) as calendar_year,
e.gender, COUNT(e.emp_no) as num_of_employees
FROM
t_employees e
JOIN
t_dept_emp d on d.emp_no=e.emp_no
GROUP BY calendar_year, e.gender
HAVING calendar_year>=1990;


#2

SELECT 
YEAR(d.from_date) as calendar_year,
e.gender, COUNT(e.emp_no) as num_of_employees
FROM
t_employees e
JOIN
t_dept_emp d on d.emp_no=e.emp_no
INNER JOIN
t_dept_manager m ON m.emp_no=e.emp_no
GROUP BY calendar_year, e.gender
HAVING calendar_year>=1990;


#3

SELECT 
YEAR(d.from_date) as calendar_year,
e.gender, COUNT(e.emp_no) as num_of_employees,SUM(s.salary),de.dept_name
FROM
t_employees e
JOIN
t_dept_emp d on d.emp_no=e.emp_no
#INNER JOIN
#t_dept_manager m ON m.emp_no=e.emp_no
JOIN
t_salaries s ON s.emp_no=e.emp_no
JOIN
t_departments de ON de.dept_no=d.dept_no
GROUP BY calendar_year, e.gender,de.dept_name
HAVING calendar_year>=1990;
