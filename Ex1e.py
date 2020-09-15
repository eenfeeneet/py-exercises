import math

def main():
	a = 2
	b = 5
	c = 2.5
	d = 6.5
	e = 2 + 6j
	f = 4 - 5j

	list11=["RACE","is","GREAT"]
	tuple1=["RACE","is","AMAZING"]
	list1 = [a,b,c,d,e,f]
	list1 = list1 + list11
	print list1
	print(a**6)
	print(b**8)
	print(e**0.5)
	print("r is ", c%d)
	print("div is", e/f)
	print("floor div is", e//f)
	print(tuple1)
	newTuple1 = tuple1[0] + " " + tuple1[1] + " " + tuple1[2]
	print(newTuple1*3)
	tuple1[-1] = "GREAT" # o
	print(tuple1)
	list1.append("ALWAYS")
	print(list1)
	list2=["PYTHON", "IS", "AMAZING"]
	list1.insert(2,list1) #qi
	print(list1)
	list1.extend(list2) #qii
	print list2
	list2.remove("IS")
	print("list2 is", list2) #QIII
	list2.reverse()
	print list2
	list1.sort()
	print list1




if __name__ == '__main__':
		main()