import math
from random import *
from tabulate import tabulate
H = {}
R = {}

def main():
	
	for i in range (1,41):
		H.update ( {'Student' + str(i) :randint(0,100)}) # generates random scores for all students in dictionary

	headers = ['name','score']
	data = sorted([(v,k) for v,k in H.items()])

	print(tabulate(data,headers=headers))
	#print(data)

	rewardsHeaders = ['reward', 'headcount']
	
	coffeebean = CheckScores(60,79,'coffeebean') #sends lower and upper scores to function that finds hits within range
	starbucks = CheckScores(80,95,'starbucks') #repeat
	korea = CheckScores(96,100,'korea')
	nextTime = CheckScores(0,59,'Next time') #total length of H minus everything else

	#print(tabulate(R.items(),headers = rewardsHeaders))

def CheckScores (lowerScore, upperScore, reward):
	hits = 0
	for name, score in H.items():
		if lowerScore <= score <= upperScore:
			hits += 1
	R.update({reward: hits})
	return hits
	
if __name__ == '__main__':
	main()