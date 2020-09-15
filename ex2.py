import math

def main():
	for a in range(1,11):
		print(a)
	if a == 10:
		print("DONE")
	x = 1
	while x<11: 
		print (x)
		if x == 10: print ("done")
		x += 1 
	for y in range(1,11):
		if y == 10:
			print("DONE")
		else:
			print(y)
	z = 0
	while z < 10:
		z += 1
		print (z)
	else:
		print("DONE")


if __name__ == '__main__':
		main()