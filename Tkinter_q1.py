from tkinter import* #* is to include all available functions from tk inter
from shapely.geometry import polygon

coordinatesList = []
area = 0
length = 0

root = Tk()

label1 = Label(root, text = "first coordinate: ", fg= "black", bg = "white")
label1.grid(row = 1, column = 1)
entry1 = Entry(root)
entry1.grid(row=1,column = 2) #.grid specifies the position

label2 = Label(root, text = "second coordinate: ", fg= "black", bg = "white")
label2.grid(row = 2, column = 1)
entry2 = Entry(root)
entry2.grid(row=2,column = 2) #.grid specifies the position

label3 = Label(root, text = "third coordinate: ", fg= "black", bg = "white")
label3.grid(row = 3, column = 1)
entry3 = Entry(root)
entry3.grid(row=3,column = 2) #.grid specifies the position

label4 = Label(root, text = "fourth coordinate: ", fg= "black", bg = "white")
label4.grid(row = 4, column = 1)
entry4 = Entry(root)
entry4.grid(row=4,column = 2) #.grid specifies the position

label7 = Label(root, text = "area: ", fg = "black", bg = "white")
label7.grid(row = 5, column = 1,sticky = E)
label8 = Label(root, text = "length: ", fg = "black", bg = "white")
label8.grid(row = 6, column = 1, sticky = E)

def Generate():

	coordinates1 = entry1.get()
	coordinates2 = entry2.get()
	coordinates3 = entry3.get()
	coordinates4 = entry4.get()
	coordinatesAll = coordinates1 + "," + coordinates2 +"," + coordinates3 +"," + coordinates4
	splitList = coordinatesAll.split(",")
	# global coordinatesList
	# for i in splitList:
	# 	coordinatesList.append(int(i))
	# print(coordinatesList)
	# canvas1.create_polygon(coordinatesList[0],coordinatesList[1],coordinatesList[2],coordinatesList[3],coordinatesList[4],coordinatesList[5],coordinatesList[6],coordinatesList[7])
	for x in range (0,len(splitList)):
		if x%2 == 0:
			coordinatesList.append((float(splitList[x]),float(splitList[x+1])))
	polygon1 = polygon.Polygon(coordinatesList)
	canvas1.create_polygon(coordinatesList)
	area = round (polygon1.area,3)
	length = round( polygon1.length,3)
	print(area)
	print(length)
	label5 = Label(root, text = area, fg = "black", bg = "yellow")
	label5.grid(row = 5, column = 2)
	label6 = Label(root, text = length, fg = "black", bg = "yellow")
	label6.grid(row = 6, column = 2)

def Clear():
	coordinatesAll=""
	canvas1.delete(polygon1)

button1 = Button(root,text="generate",command = Generate, fg="white",bg="blue")
button1.grid(row = 7, column = 2)

button2 = Button(root,text="clear",command = Clear, fg="white",bg="blue")
button2.grid(row = 8, column = 2)

canvas1 = Canvas(root,width = 300, height = 300, bg = "green")
canvas1.grid(row=5,column=3)

root.mainloop()
