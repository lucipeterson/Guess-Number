#guessnumber.py
import random

print("~~ Guess the Number ~~")
print("I am thinking of a number between 1 and 100.  You have 10 chances to guess what it is.  Good luck!")

number = random.randint(1, 101)
guess = int(input("What number am I thinking of? "))

#print(number) to test winning scenario

counter = 1
while guess != number:
    guess = int(input("What number am I thinking of? "))
    counter += 1
    if counter == 10:
        print("The number was " + str(number) + ".")
        print("Game Over")
        break

if guess == number:
    print("Congratulations! You guessed it!")
