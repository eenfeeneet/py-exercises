from Tkinter import*

class Window(object):

	def __init__(self,master):
		self.master = master
		self.sizeInput = StringVar()
		self.toppingInput = StringVar()

		master.title('pizzahut')
		master.geometry('700x400')
		master.resizable(width=False,height=False)

		self.leftFrame = Frame(master,width = 300, height = 400)
		self.leftFrame.grid(row = 0,column=0)
		self.rightFrame = Frame(master,width = 400, height = 400)
		self.rightFrame.grid(row = 0,column = 1)
		self.canvas = Canvas(self.rightFrame,width=400,height=400,bg="white")
		self.canvas.pack()

		self.r1 = Radiobutton(self.leftFrame,	text='small',	variable=self.sizeInput,	command=self.UpdateCanvas, value='small').grid(row=0)
		self.r2 = Radiobutton(self.leftFrame,	text='medium',	variable=self.sizeInput,	command=self.UpdateCanvas, value = 'medium').grid(row=1)
		self.r3 = Radiobutton(self.leftFrame,	text='big',		variable=self.sizeInput,	command=self.UpdateCanvas, value = 'big').grid(row=2)
		self.r4 = Radiobutton(self.leftFrame,	text='pepperoni',	variable=self.toppingInput,	command=self.UpdateCanvas, value = 'pepperoni').grid(row=3)
		self.r5 = Radiobutton(self.leftFrame,	text='capsicum',	variable=self.toppingInput,	command=self.UpdateCanvas, value = 'capsicum').grid(row=4)
		self.r6 = Radiobutton(self.leftFrame,	text='cheese',	variable=self.toppingInput,	command=self.UpdateCanvas, value = 'cheese').grid(row=5)
		self.buttonAdd = Button(self.leftFrame, text='ADD', command= self.AddToListBox)
		self.buttonAdd.grid(row=6)
		self.cartLabel = Label(self.leftFrame, text = 'CART').grid(row=7,pady=10)
		self.listBox = Listbox(self.leftFrame,width = 25) #has to be written this way or it wont work
		self.listBox.grid(row=8, sticky = '')
		self.totalPriceLabelOutput = Label(self.leftFrame) #has to be written this way or it wont work
		self.totalPriceLabelOutput.grid(row =9)
		self.buttonRemove = Button(self.leftFrame, text = 'REMOVE', command= self.RemoveFromListBox)
		self.buttonRemove.grid(row=10)

	def UpdateCanvas(self):

   		self.canvas.delete('all')
   		center = 200 # center of circle coordinate (200,200)
   		r = 0
   		color = ''
   		if self.sizeInput.get() == 'small':	
   			r = 50
   		elif self.sizeInput.get() =='medium':
   			r = 90
   		elif self.sizeInput.get() == 'big':
   			r = 140
   		if self.toppingInput.get() == 'pepperoni':
   			color = 'brown'
   		elif self.toppingInput.get() == 'capsicum':
   			color = 'green'
   		elif self.toppingInput.get() == 'cheese':
   			color = 'yellow'
   		self.canvas.create_oval(center-r-10,center-r-10,center+r+10,center+r+10,width=4,fill='tan1')
   		self.MakeCircularArray(r,color)
   		
   	def MakeCircularArray(self,size,color):
		z = 20 #steps in moving from point to point
		for x in range(0,400,z): 
			for y in range (0,400,z):
				if ((x-200)**2 + ((y-200)**2))**0.5 <= size:
					self.MakeCircle(x,y,8,color) #8 is radius of circle object

	def MakeCircle(self,x,y,r,color):
		return self.canvas.create_oval(x-r,y+r,x+r,y-r,fill=color)

	def AddToListBox(self):

		Pizza.AddPizza(self.sizeInput.get(),self.toppingInput.get())
		self.listBox.insert(END,'{} {} pizza : ${}'.format(Pizza.cart[-1].size,Pizza.cart[-1].topping,Pizza.cart[-1].price))
		self.UpDateTotalPrice()
		
	def RemoveFromListBox(self):
		
		try:
			sel = self.listBox.curselection() #this is return a list of indexes
			self.listBox.delete(sel)
			intsel = sel[0]
			Pizza.RemovePizza(intsel)
		except Exception:
			pass		
		self.UpDateTotalPrice()

	def UpDateTotalPrice(self):
		totalPrice = 0
		for index in range (0, len(Pizza.cart)):
			totalPrice = totalPrice + Pizza.cart[index].price
		self.totalPriceLabelOutput.config(text = 'total price:${}'.format(totalPrice))

class Pizza(object):

	ingredients = {'small':5,'medium':10,'big':20,'pepperoni':5,'capsicum':2,'cheese':3}
	cart =[]  #class attribute that stores list of added objects

	def __init__(self,size,topping):
		self.size = size
		self.topping = topping
		price1= self.ingredients.get(size)
		price2= self.ingredients.get(topping)
		self.price = price1 + price2

	def __str__(self):
		return '{} {} :${}'.format(self.size,self.topping,self.price)

	@classmethod
	def AddPizza(cls,size,topping):
		'''create pizza object and add into cart'''
		pizza = Pizza(size,topping)
		cls.cart.append(pizza)

	@classmethod
	def RemovePizza(cls,sel):
		cls.cart.pop(sel) #remove pizza object by index. sel from listbox is the same index as items[]

def main():

	root= Tk()
	window = Window(root)
	root.mainloop()

if __name__ == '__main__':
	main()