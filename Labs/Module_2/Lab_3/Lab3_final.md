



# Lab | Statistics Foundations









## Challenges


## Part 1


### Challenge 1


Find a and b, if median=42, mean=50


20,34, 34,  12, 56, 110, 49, a, b.







/determine a :


a = 42 because the median is 42 and it misses this number in the list


which has an odd number of item.







/determine b with simple math :


(315 + 42 + b )/9 = 50


b = 93







### Challenge 2


A car hit an average speed of v1 = 60 kmph in the first half of the journey, and hit an average speed of v2 = 110 kmph in the second half of the journey. Determine the average speed of the car.







the driver drives 50% of the day at 60mph and 50% at 110 mph:


avg_speed = 60 * 0,5 + 110 * 0,5 = 85












### Challenge 3


The lifetimes of 400 light-bulbs were found to the nearest hour. The results were recorded as


follows.


Lifetime (hours) 0–199 200–399 400–599 600–799 800–999 1000–1199 1200–1999


Frequency         143     97      64      51      14      14        17


Construct a histogram and cumulative frequency polygon for this dataset. Estimate the percentage


of bulbs with lifetime less than 480 hours.







**See the pictures in the lab file to see the histograms.**


The percentage of bulbs with lifetime less than 480 hours is about 64%.







### Challenge 4


The time between arrival of 60 patients at an intensive care unit were recorded to the nearest hour.


The data are shown below.


Time (hours) 0–19 20–39 40–59 60–79 80–99 100–119 120–139 140–159 160–179


Frequency     16    13    17    4     4      3       1      1       1


Determine the median, mean and standard deviation for this dataset.







See the pictures attached to see the calculations


median = 38.8


mean = 46.5


std = 26.03

Mean Calculation

Midpoint	9.5	29.5	49.5	69.5	89.5	109.5	129.5	149.5	169.5
Frequency*Midpoint	152	383.5	841.5	278	358	328.5	129.5	149.5	169.5
									
a=sum(Frequency*Midpoint)	2790								
mean=a/sum(Frequency)	46.5								




## Part 2


### Challenge 1


One player rolls two dices. Describe the measurable space and the random variable for:


* A. The values that the player obtains.


* B. The sum of the values obtained.


* C. The maximum value obtained after rolling both dices.







A={(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),


(2,2),(2,3),(2,4),(2,5),(2,6),


(3,3),(3,4),(3,5),(3,6),


(4,4),(4,5),(4,6),


(5,5),(5,6),


(6,6)}







B={2,3,4,5,6,7,4,5,6,7,8,6,7,8,9,10,11,12}







C={12}







Describe the following events:


* Case A: Both values are greater than 5.


* Case B: The sum of values is even.


* Case C: The maximum is the value of both rolls.







CaseA = {(6,6)}


P(X=CaseA) = 1/21







CaseB


P(X=CaseB) = 11/18







CaseC


P(X=CaseC) = 1







### Challenge 2


One player picks two cards from a poker deck. Describe the measurable space and the random variable for:


* A. The number of figures he picks.


* B. The sum of card values. Consider that the value of figures is 10 and the value of aces is 15.


* C. The number of hearts or spades he picks.







A/ clubs=c, Diamonds=d,hearts=h, spades=s


S={(c,c),(c,d),(c,h),(c,s),(d,d),(d,h),(d,s),(h,h),(h,s),(s,s)}


B/


S={4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25}


C/


S={(c,h),(c,s),(d,h),(d,s),(h,h),(h,s),(s,s)}







Describe the following events:


* Case A: The number of figures in the cards the player picked is two.


* Case B: The sum of card values is 17.


* Case C: The value of both cards is less than 8.







case A/


S={(c,d),(c,h),(c,s),(d,h),(d,s),(h,s)}


P(X=S) = 6/10







case B/ S={(7,10),(8,9),(10,7),(J,7),(Q,7),(K,7),(A,2)}


P(X=S) = 8/78.


total possibilities=13!/2!(13-2)!







case C/ S={(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(4,2),(4,3),(5,2)}


P(X=S) = 10/78












### Challenge 3


Two players roll a dice. Describe the measurable space and the random variable for:


* A. The score of player A.


* B. The greatest score.


* C. The earnings of player A if the game rules state that: 


"The player with the greatest score gets a coin from the other player.".


* D. The earnings of player A if the game rules state that: 


"The player with the greatest score gets as many coins as the difference between the score of player A and player B.".







Describe the following events:


* Case A: The score of player A is 2.


* Case B: The greatest score is lower or equal than 2.


* Case C: Considering the case where the winner gets as many coins as the difference between scores (D), describe:


 * Player A wins at least 4 coins.


 * Player A loses more than 2 coins.


 * Player A neither wins nor loses coins.






A.


S={(1,2,3,4,5,6)}


Case A:


P(X=CaseA) = 1/6







B.


s={(A1,B1),(A1,B2),(A2,B1),(A2,B2)}


Case B:


P(X=CaseB)=4/36







C.


S={-1,0,1}







CaseC1


S = {(A5,B1),(A6,B1),(A2,B6),(A6,B2),(A1,B6),(A1,B5)}


P(X=CaseC1) = 1/6







CaseC2


S = {(A2,B5),(A2,B6),(A3,B6),(A1,B4),(A1,B5),(A1,B6)}


P(X=CaseC2) = 1/6







CaseC3


S = {(A1,B1),(A2,B2),(A3,B3),(A4,B4),(A5,B5),(A6,B6)}


P(X=CaseC3) = 1/6







