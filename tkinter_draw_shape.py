from tkinter import*
from shapely.geometry import polygon

class drawShape(object):
	"""docstring fos drawShape"""
	def __init__(self, master):
		self.master = master
		master.title("Draw Shape")
		"""root.geometry('{}x{}'.format(<widthpixels>,<heightpixels>))"""
		master.geometry("{}x{}".format(700,500))
		master.resizable(width=False,height=False)

		master.grid_rowconfigure(1,weight=1)
		master.grid_columnconfigure(0,weight=1)

		#Create layout
		self.LeftFrame = Frame(master,width=350,height=500,bd=2,relief=RAISED)
		self.RightFrame = Frame(master,width=350,height=500,bd=4,relief=SUNKEN)

		self.LeftFrame.grid(row=0,sticky=W)
		self.RightFrame.grid(row=0,sticky=E)

		#Create widget
		self.label1 = Label(self.RightFrame,text="Enter coordinates of polygon(x1,x2,...,xn,yn)")
		self.entry1 = Entry(self.RightFrame)
		self.okButton = Button(self.RightFrame,text="OK",command=self.calculate)

		self.canvas = Canvas(self.LeftFrame,width=350,height=490,bg="white")
		# self.label2 = Label(self.LeftFrame,text="Area: ")
		self.Area = StringVar(self.LeftFrame,value="0")
		self.areaLabel = Label(self.LeftFrame,textvariable=self.Area)
		self.Perimeter = StringVar(self.LeftFrame,value="0")
		self.perimaterLabel = Label(self.LeftFrame,textvariable=self.Perimeter)

		# Layout
		self.label1.grid(row=0,column=0)
		self.entry1.grid(row=1,column=0)
		self.okButton.grid(row=2,column=0)

		self.canvas.grid(row=0,column=0)
		# self.label2.grid(row=0,sticky=NW)
		self.areaLabel.grid(row=0,column=0,sticky=SW)
		self.perimaterLabel.grid(row=0,column=0,sticky=SE)

		# functionality
	def calculate(self):
		list1 = self.entry1.get().split(",")
		array1 = []
		i = 0
		for x in range(0,len(list1)):
			if x%2 == 0:
				array1.append((int(list1[x]),int(list1[x+1])))
		print(array1)
		polygon1 = polygon.Polygon(array1)
		print(polygon1.area)
		self.Area.set(polygon1.area)
		self.Perimeter.set(polygon1.length)
		self.canvas.create_polygon(array1)

def main():
	root = Tk()
	gui = drawShape(root)
	root.mainloop()
if __name__ == '__main__':
	main()