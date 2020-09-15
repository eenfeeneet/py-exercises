import math
from random import *

def main():
	randomNumber = 0
	count = 0
	number = int (input(print("enter a number between 1 to 50 for me to guess")))
	while number != randomNumber:

		randomNumber = randint(1,50)
		print (randomNumber)
		count += 1

	print("Your number is " + str(randomNumber) + " after " + str(count) + " guesses.")

if __name__ == '__main__':
	main()