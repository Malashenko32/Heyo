import random
import math

name = input("What is your name, dear stranger?: ")
print ("Hey " + str(name) + " can you guess what number from 1 to 10 I'm thinking right now?: ")
number = random.randint(1, 10)
lives = 3
while lives > 0:
	answer = int(input())
	if answer == number:
		print ("Congratulations! You won the game!")
		break
	elif answer > number:
		lives = lives - 1
		print ("Oops! It's lower than that!")
		print ("Sorry, try again! You only have " + str(lives) + " Guesses left")
	elif answer < number:
		lives = lives - 1
		print ("Oops! It's higher than that!")
		print ("Sorry, try again! You only have " + str(lives) + " Guesses left")
if lives == 0:
	print ("Game Over")