
import math

def main ():

	no1 = int(input("enter 1st number:"))
	no2 = int(input("enter 2nd number:"))

	print ("results"+'\n'+str(Addition(no1,no2))+'\n'+str(Subtraction(no1,no2))+'\n'+str(Multiply(no1,no2))+'\n'+str(Division(no1,no2)))
def Addition (no1 , no2):
	return no1 + no2
def Subtraction (no1 , no2):
	return no1 - no2
def Multiply (no1, no2):
	return no1 * no2
def Division (no1, no2):
	return no1/no2

if __name__ == '__main__':
	main()
