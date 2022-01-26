#1. From the order_items table, find the price of the highest priced order and lowest price order.
#lowest price order
SELECT order_id,price
FROM olist.order_items
ORDER BY price ASC
LIMIT 1;

#highest priced
SELECT order_id,price
FROM olist.order_items
ORDER BY price DESC
LIMIT 1;


#2. From the order_items table, what is range of the shipping_limit_date of the orders?
SELECT MAX(shipping_limit_date)-MIN(shipping_limit_date) as Range_Shipping
FROM olist.order_items


#3. From the customers table, find the states with the greatest number of customers.
SELECT customer_state,COUNT(customer_state) as counter
FROM olist.customers
GROUP BY customer_state
ORDER BY counter DESC
LIMIT 1;

#4. From the customers table, within the state with the greatest number of customers, find the cities with the greatest number of customers.
SELECT customer_city,count(customer_city)
FROM olist.customers WHERE customer_state='SP'
GROUP BY customer_city
ORDER BY count(customer_city) DESC
LIMIT 10;

#5. From the closed_deals table, how many distinct business segments are there (not including null)?
SELECT COUNT(DISTINCT business_segment)
FROM olist.closed_deals WHERE business_segment is not NULL;


#6. From the closed_deals table, sum the declared_monthly_revenue for duplicate row values in business_segment and find the 3 business segments with the highest declared monthly revenue (of those that declared revenue).

SELECT business_segment,SUM(declared_monthly_revenue)
FROM olist.closed_deals WHERE business_segment is not NULL
GROUP BY business_segment
ORDER BY SUM(declared_monthly_revenue) DESC
LIMIT 3;

#7. From the order_reviews table, find the total number of distinct review score values.

SELECT COUNT(DISTINCT review_score)
FROM olist.order_reviews;

#8. In the order_reviews table, create a new column with a description that corresponds to each number category for each review score from 1 - 5, then find the review score and category occurring most frequently in the table.

ALTER TABLE olist.order_reviews
 ADD comments TEXT;


update olist.order_reviews set comments = "Very bad"
WHERE review_score=1;

update olist.order_reviews set comments = "Bad"
WHERE review_score=2;

update olist.order_reviews set comments = "Not Bad not Good"
WHERE review_score=3;

update olist.order_reviews set comments = "Good"
WHERE review_score=4;

update olist.order_reviews set comments = "Excellent"
WHERE review_score=5;

SELECT review_score,count(review_score)
FROM olist.order_reviews
GROUP BY review_score
ORDER BY count(review_score) DESC
LIMIT 1;



SELECT comments,count(comments)
FROM olist.order_reviews
GROUP BY comments
ORDER BY count(comments) DESC
LIMIT 1;


#9. From the order_reviews table, find the review value occurring most frequently and how many times it occurs.

SELECT review_score,count(review_score)
FROM olist.order_reviews
GROUP BY review_score
ORDER BY count(review_score) DESC
LIMIT 1;

