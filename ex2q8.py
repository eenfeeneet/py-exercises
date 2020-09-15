import math

def main():
	name = "determine"
	print name
	libCount = len(name)
	print ("using library func: " + str(libCount))
	nonLibCount = CountChar(name)
	print ("using non library func: " + str(nonLibCount))

def CountChar(word):
	count = 0
	for char in word:
		count += 1
	return count

if __name__ == '__main__':
	main()