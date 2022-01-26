USE publications;


SELECT au_id,SUM(TOTAL) AS Suma
FROM
(SELECT au_id, (sales_total+Advance_total) AS TOTAL
FROM (SELECT title_id,au_id,SUM(sales_royalty) AS sales_total, SUM(Advance) AS Advance_total
FROM (SELECT titles.title_id,titleauthor.au_id,(titles.advance * titleauthor.royaltyper / 100) AS Advance,(titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100) AS sales_royalty
FROM titles
JOIN sales
ON titles.title_id=sales.title_id
JOIN titleauthor
ON titles.title_id=titleauthor.title_id) nombre_query
GROUP BY titles.title_id,titleauthor.au_id) sub_query) sub_sub_query
GROUP BY au_id
ORDER BY Suma DESC
LIMIT 3;

#CHALLENGE 2, WITH TEMPORARY TABLES
CREATE TEMPORARY TABLE primera
SELECT titles.title_id,titleauthor.au_id,(titles.advance * titleauthor.royaltyper / 100) AS Advance
FROM titles
JOIN sales
ON titles.title_id=sales.title_id
JOIN titleauthor
ON titles.title_id=titleauthor.title_id
GROUP BY title_id,au_id;

CREATE TEMPORARY TABLE segunda
SELECT titles.title_id,(titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100) AS sales_royalty
FROM titles
JOIN sales
ON titles.title_id=sales.title_id
JOIN titleauthor
ON titles.title_id=titleauthor.title_id;

CREATE TEMPORARY TABLE tercera
SELECT primera.au_id,(primera.Advance+segunda.sales_royalty) AS Total
FROM  primera
JOIN segunda
ON primera.title_id=segunda.title_id;

CREATE TEMPORARY TABLE Final
SELECT tercera.au_id,SUM(Total) AS suma
FROM tercera
GROUP BY tercera.au_id
ORDER BY suma DESC
LIMIT 3;

#CHALLENGE 3

CREATE TABLE permanent
SELECT * FROM Final


