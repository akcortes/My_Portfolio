select * from apple.applestore;

#1. What are the different genres?
select prime_genre from apple.applestore;

#2. Which is the genre with the most apps rated?
SELECT prime_genre, SUM(rating_count_tot) as ana
FROM apple.applestore
GROUP BY prime_genre
ORDER BY ana DESC
LIMIT 1;





#3. Which is the genre with most apps?
SELECT prime_genre,COUNT(prime_genre) as Total
FROM apple.applestore
GROUP BY prime_genre
ORDER BY Total DESC
LIMIT 1;

#4. Which is the one with least?
SELECT prime_genre,COUNT(prime_genre) as Total
FROM apple.applestore
GROUP BY prime_genre
ORDER BY Total ASC
LIMIT 1;

#5. Find the top 10 apps most rated.
SELECT track_name, rating_count_tot 
FROM apple.applestore
ORDER BY rating_count_tot DEsC
LIMIT 10;


#6. Find the top 10 apps best rated by users.
SELECT track_name, user_rating
FROM apple.applestore
ORDER BY user_rating DESC
LIMIT 10;

#7. Take a look at the data you retrieved in question 5. Give some insights.
SELECT track_name, rating_count_tot, user_rating
FROM apple.applestore
ORDER BY rating_count_tot DEsC
LIMIT 10;
#The rating count of Facebook is very far from the others apps. 2 from top 3 of ratings are related to social media apps

#8. Take a look at the data you retrieved in question 6. Give some insights.
SELECT track_name, user_rating,rating_count_tot
FROM apple.applestore
ORDER BY user_rating DESC
LIMIT 10;
#The user rating could be high because the number of rating_count_total are very low . There are some apps with only 1 rating: It's not possible to afirm these are the bests apps

#9. Now compare the data from questions 5 and 6. What do you see?
#In order to determine any hypothesis regarding the data it's necessary 
#to focus on different data elements. It's important to compare different perspectives.
# For example, Pinterest, whose user rate is 4_5 is not in the top 5 of best apps rates for the user, however, regarding the number of users that have voted,
# I could say it 's one of hte best apps regarding the user votes

#10. How could you take the top 3 regarding both user ratings and number of votes?
SELECT track_name, user_rating,rating_count_tot
FROM apple.applestore
ORDER BY  user_rating and rating_count_tot  DESC
LIMIT 3;

#11. Do people care about the price of an app? Do some queries, comment why are you doing them and the results you retrieve. What is your conclusion?
SELECT track_name, price,rating_count_tot,user_rating
FROM apple.applestore
ORDER BY  price  DESC
LIMIT 15;

#Yes, people do care about the price of an app. Data shows the top 15 more expensives apps have less reting count total, even if the user rating is higher than 4:

