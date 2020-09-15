import math

def main():
	i = 0
	x = ""
	while (i<9):
		if i<5:
			x = x + str(i+1)
			print(x)
		else:
			print(x[0:9-i]) #splicing [start:end]
		i += 1

if __name__ == '__main__':
	main()