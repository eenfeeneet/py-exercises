
numberCheck = 11

def CheckPrime(number):

	divisor = numberCheck -1
	flag = True

	while divisor > 1:
		if numberCheck % divisor == 0:
			flag = False
			break
		else:
		 divisor -= 1
	return flag

if (CheckPrime(numberCheck) == True):
	print ("is a prime number")

else:
	print ("not a prime number")

