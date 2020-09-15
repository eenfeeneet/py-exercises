from tkinter import*
from shapely.geometry import polygon

class Window(object):
	def __init__(self,master):
		self.master = master
		self.size = StringVar()
		self.topping = StringVar()

		master.title('polygon shaping')
		master.geometry('800x800')
		master.resizable(width=False,height=False)

		master.grid_rowconfigure(1,weight=1)
		master.grid_columnconfigure(1,weight=1)

		# defining frames
		self.topLeftFrame = Frame(master,width=400,height=400,bd=2)
		self.topLeftFrame.grid(row=0,column=0)
		self.topRightFrame = Frame(master,width=400,height=400,bd=2)
		self.topRightFrame.grid(row=0,column=1)
		self.bottomLeftFrame = Frame(master,width=400,height=400,bd=2)
		self.bottomLeftFrame.grid(row=1,column=0)
		self.bottomRightFrame = Frame(master,width=400,height=400,bd=2,bg="yellow",relief=SUNKEN)
		self.bottomRightFrame.grid(row=1,column=1)
		self.radioButtonsFrame1 = Frame(self.topRightFrame, width = 200, height=400,bg='white')
		self.radioButtonsFrame1.grid(row=0)
		self.radioButtonsFrame2 = Frame(self.topRightFrame, width = 200, height=400,bg='sky blue')
		self.radioButtonsFrame2.grid(row=1)

		# trying out labels on top left frame
		self.label1 = Label(self.topLeftFrame,text="PIZZA SELECTION",font=(NONE,30))
		self.label1.grid(row=0)



		#building radio buttons on top right frame
		self.r1 = Radiobutton(self.radioButtonsFrame1, text="small", variable=self.size, value='small', command=self.UpdateCanvas)
		self.r1.grid(row=0)
		self.r2 = Radiobutton(self.radioButtonsFrame1, text="medium", variable=self.size, value='medium', command=self.UpdateCanvas)
		self.r2.grid(row=1)
		self.r3 = Radiobutton(self.radioButtonsFrame1, text="big", variable=self.size, value='big', command=self.UpdateCanvas)
		self.r3.grid(row=2)
		self.TRlabel = Label(self.radioButtonsFrame1,text='you have selected:')
		self.TRlabel.grid(row=3)
		self.TRLabelOutput = Label(self.radioButtonsFrame1)
		self.TRLabelOutput.grid(row=4)

		#building radio buttons on bottom left frame
		self.r4 = Radiobutton(self.radioButtonsFrame2, text = 'pepperoni', variable=self.topping, value = 'pepperoni', command=self.UpdateCanvas)
		self.r4.grid(row=0)
		self.r5 = Radiobutton(self.radioButtonsFrame2, text = 'chicken', variable=self.topping, value='chicken', command = self.UpdateCanvas)
		self.r5.grid(row=1)
		self.r6 = Radiobutton(self.radioButtonsFrame2, text = 'beef', variable=self.topping, value='beef', command = self.UpdateCanvas)
		self.r6.grid(row=2)

		# drawing object on bottom right frame
		center = 200 # center of circle coordinate (200,200)
		self.canvas = Canvas(self.bottomRightFrame,width=390,height=390,bg="white")
		self.canvas.grid(row=0,column=0)
		self.sml = self.canvas.create_oval(center-50,center-50,center+50,center+50,width=4,state=HIDDEN,fill='tan1')	
		self.med = self.canvas.create_oval(center-100,center-100,center+100,center+100,width=4,state=HIDDEN,fill='tan1')
		self.big = self.canvas.create_oval(center-150,center-150,center+150,center+150,width=4,state=HIDDEN,fill='tan1')
		self.MakeCircularArray(150,'brown')

	def MakeCircularArray(self,size,color):
		for x in range(0,400,20):
			for y in range (0,400,20):
				if ((x-200)**2 + ((y-200)**2))**0.5 <= size:
					self.MakeCircle(x,y,8,color)

	def MakeCircle(self,x,y,r,color):
		return self.canvas.create_oval(x-r,y+r,x+r,y-r,fill=color)

	def UpdateCanvas(self):
   		self.TRLabelOutput.config(text = self.size.get())
   		if self.size.get() == 'small':
   			self.canvas.itemconfig(self.sml,state=NORMAL)
   			self.canvas.itemconfig(self.med,state=HIDDEN)
   			self.canvas.itemconfig(self.big,state=HIDDEN)
   		elif self.size.get() == 'medium':
   			self.canvas.itemconfig(self.sml,state=HIDDEN)
   			self.canvas.itemconfig(self.med,state=NORMAL)
   			self.canvas.itemconfig(self.big,state=HIDDEN)
   		elif self.size.get() == 'big':
   			self.canvas.itemconfig(self.sml,state=HIDDEN)
   			self.canvas.itemconfig(self.med,state=HIDDEN)
   			self.canvas.itemconfig(self.big,state=NORMAL)

def main():
	root= Tk()
	window = Window(root)
	root.mainloop()

if __name__ == '__main__':
	main()