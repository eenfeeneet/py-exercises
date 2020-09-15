
number = 6

def Factorial(number):
	if number == 0:
		return 1
	else:
		return number * Factorial(number-1)

print (Factorial(number))