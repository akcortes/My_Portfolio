I reviewed the code of grupo 6

* Look for things he/she made that you think could be useful for you.

- It was a clear code. Easy to understand 
- I learned about the replete library

* What should be improved?

- less if elif else conditions , use while instead: there are a lot of if/else/elif conditions




* My suggestion with a simple modifiation 

Original code:



choice = input("Do you want to play blackjack? 'y' or 'n': ")  # Prompting the player to play a game of BlackJack

if choice == "y":
     #the code

My suggestion:

The input for the question if the user wants to play or not does not have any action if the answer is ’no’ : I would repeat the question in case the user says no and until the user says ‘yes’

choice = input("Do you want to play blackjack? 'y' or 'n': ")  # Prompting the player to play a game of BlackJack


while choice == “n”:
      choice = input("Do you want to play blackjack? 'y' or 'n': ")  # Prompting the player to play a game of BlackJack

while choice == "y":
     #the code
