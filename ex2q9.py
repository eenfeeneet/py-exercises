import math


def main():
	name = "ethan"
	charList = []
	# charList = list(name)
	# print charList
	for i in range (0,len(name)):
		charList.insert(i,name[i])
	print charList

if __name__ == '__main__':
	main()