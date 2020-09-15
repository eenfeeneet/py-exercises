import math
class Point(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y

class Line(Point):
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2
	def CalculateLength(self):
		p1 = self.p1
		p2 = self.p2
		return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2 )**0.5

class Polygon:
	def __init__(self,l1,l2,l3,l4):
		self.l1 = l1
		self.l2 = l2
		self.l3 = l3
		self.l4 = l4

	def CalculateArea(self):
		p1 = self.l1.p1
		p2 = self.l1.p2 
		p3 = self.l2.p2
		p4 = self.l3.p1
		return ((p1.y * p2.x + p2.y * p3.x + p3.y * p4.x) - (p1.x * p2.y + p2.x * p3.y + p3.x * p4.y))/2

	def CalculatePerimeter(self):
		l1 = self.l1
		l2 = self.l2
		l3 = self.l3
		l4 = self.l4
		return l1.CalculateLength() + l2.CalculateLength() + l3.CalculateLength() + l4.CalculateLength()

def main():
	point1 = Point(0,0)
	point2 = Point(0,1)
	point3 = Point(1,2)
	point4 = Point(1,0)
	line1 = Line(point1,point2)
	line2 = Line(point2,point3)
	line3 = Line(point3,point4)
	line4 = Line(point4,point1)

	print (line1.CalculateLength())
	polygon1 = Polygon(line1,line2,line3,line4)
	print("Area is {}".format( polygon1.CalculateArea()))
	perimeter = polygon1.CalculatePerimeter() #calculate perimeter
	perimeter = round(perimeter,3)	#round to 2 sig figs
	print("Perimeter is {}".format(perimeter))

if __name__ == '__main__':
	main()