def main():
	val = input("enter 2 numbers seperated by comma (x,y): ")
	inVal = val.split(",")
	print(type(val[0]))
	if (type(val[0] == int)):
		print("yes it is not a string")

	print(inVal)

if __name__ == '__main__':
	main()