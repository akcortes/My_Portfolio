#CHALLENGE 1

CREATE TEMPORARY TABLE new_tbl
SELECT authors.au_id,authors.au_lname,authors.au_fname,titleauthor.title_id
FROM authors
INNER JOIN titleauthor ON titleauthor.au_id=authors.au_id;

SELECT *
FROM new_tbl;

CREATE TEMPORARY TABLE new_tbl6
SELECT new_tbl.au_id,new_tbl.au_lname,new_tbl.au_fname,titles.title,titles.pub_id
FROM new_tbl
INNER JOIN titles ON titles.title_id=new_tbl.title_id;

SELECT *
FROM new_tbl6;


CREATE TEMPORARY TABLE new_tbl8
SELECT new_tbl6.au_id,new_tbl6.au_lname,new_tbl6.au_fname,new_tbl6.title,publishers.pub_name
FROM new_tbl6
INNER JOIN publishers ON publishers.pub_id=new_tbl6.pub_id;

SELECT *
FROM new_tbl8;

#CHALLENGE 2

SELECT new_tbl8.au_id,new_tbl8.pub_name,count(new_tbl8.title)
FROM new_tbl8
GROUP BY new_tbl8.au_id,new_tbl8.pub_name;

#CHALLENGE 3

CREATE TEMPORARY TABLE new_tbl20
SELECT authors.au_id,authors.au_lname,authors.au_fname,titleauthor.title_id
FROM authors
LEFT JOIN titleauthor ON titleauthor.au_id=authors.au_id;

SELECT *
FROM new_tbl20;

SELECT new_tbl20.au_id,new_tbl20.au_lname,new_tbl20.au_fname,SUM(sales.qty)
FROM new_tbl20
INNER JOIN sales ON new_tbl20.title_id=sales.title_id
GROUP BY new_tbl20.au_id,new_tbl20.au_lname,new_tbl20.au_fname
ORDER BY SUM(sales.qty) DESC
LIMIT 3;

#Challenge 4
CREATE TEMPORARY TABLE new_tbl21
SELECT new_tbl20.au_id,new_tbl20.au_lname,new_tbl20.au_fname,SUM(sales.qty) AS TOTAL
FROM new_tbl20
LEFT JOIN sales ON sales.title_id=new_tbl20.title_id
GROUP BY new_tbl20.au_id,new_tbl20.au_lname,new_tbl20.au_fname
ORDER BY TOTAL DESC;

UPDATE new_tbl21
SET new_tbl21.TOTAL= '0'
WHERE new_tbl21.TOTAL is NULL;

SELECT *
FROM new_tbl21

