from tkinter import*

class Window(object):

	def __init__(self,master):
		self.master = master
		self.sizeInput = StringVar()
		self.toppingInput = StringVar()

		master.title('pizzahut')
		master.geometry('800x400')
		master.resizable(width=False,height=False)

		self.leftFrame1 = Frame(master,width = 200, height = 200)
		self.leftFrame1.grid(row = 0,column=0)
		self.leftFrame2 = Frame(master, width = 200, height = 200)
		self.leftFrame2.grid(row =0, column=1)
		self.leftFrame3 = Frame(master, width = 400, height = 200)
		self.leftFrame3.grid(row =1, column=0, columnspan = 2)
		self.rightFrame = Frame(master,width = 400, height = 400)
		self.rightFrame.grid(row = 0,column = 2, rowspan = 2)
		self.canvas = Canvas(self.rightFrame,width=400,height=400,bg="white")
		self.canvas.pack()

		self.sizeLabel = Label(self.leftFrame1, text = 'Size', bg = 'yellow').grid(row=0)
		self.r1 = Radiobutton(self.leftFrame1,	text='small',	variable=self.sizeInput,	command=self.UpdateCanvas, value='small').grid(row=1)
		self.r2 = Radiobutton(self.leftFrame1,	text='medium',	variable=self.sizeInput,	command=self.UpdateCanvas, value = 'medium').grid(row=2)
		self.r3 = Radiobutton(self.leftFrame1,	text='big',		variable=self.sizeInput,	command=self.UpdateCanvas, value = 'big').grid(row=3)
		self.toppingLabel = Label(self.leftFrame2, text = 'Topping',bg='yellow').grid(row=0)
		self.r4 = Radiobutton(self.leftFrame2,	text='pepperoni',	variable=self.toppingInput,	command=self.UpdateCanvas, value = 'pepperoni').grid(row=1)
		self.r5 = Radiobutton(self.leftFrame2,	text='capsicum',	variable=self.toppingInput,	command=self.UpdateCanvas, value = 'capsicum').grid(row=2)
		self.r6 = Radiobutton(self.leftFrame2,	text='cheese',	variable=self.toppingInput,	command=self.UpdateCanvas, value = 'cheese').grid(row=3)
		self.specialEntryLabel = Label(self.leftFrame3, text = 'Special Instructions', bg = 'yellow').grid(row=0,column=0)
		self.specialEntry = Entry(self.leftFrame3)
		self.specialEntry.grid(row=0,column=1)
		self.buttonAdd = Button(self.leftFrame3, text='ADD', command= self.AddToListBox)
		self.buttonAdd.grid(row=1,columnspan=2)
		self.cartLabel = Label(self.leftFrame3, text = 'CART').grid(row=2,pady=10)
		self.listBox = Listbox(self.leftFrame3,width = 40) #has to be written this way or it wont work
		self.listBox.grid(row=2, columnspan = 2,sticky = "")
		self.totalPriceLabelOutput = Label(self.leftFrame3) #has to be written this way or it wont work
		self.totalPriceLabelOutput.grid(row =3, columnspan=2)
		self.buttonRemove = Button(self.leftFrame3, text = 'REMOVE', command= self.RemoveFromListBox)
		self.buttonRemove.grid(row=4,columnspan = 2)

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

		Pizza.AddPizza(self.sizeInput.get(),self.toppingInput.get(),self.specialEntry.get())
		self.listBox.insert(END,'{} {} pizza : ${} special: {}'.format(Pizza.cart[-1].size,Pizza.cart[-1].topping,Pizza.cart[-1].price,Pizza.cart[-1].special))
		self.specialEntry.delete(0,'end')
		self.UpDateTotalPrice()
		
	def RemoveFromListBox(self):
		
		try:
			sel = self.listBox.curselection() #this is return a list of indexes
			self.listBox.delete(sel)
			print (sel)
			intsel = sel[0]
			print (intsel)
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

	def __init__(self,size,topping,special):
		self.size = size
		self.topping = topping
		price1= self.ingredients.get(size)
		price2= self.ingredients.get(topping)
		self.price = price1 + price2
		self.special = special

	def __str__(self):
		return '{} {} :${}'.format(self.size,self.topping,self.price)

	@classmethod
	def AddPizza(cls,size,topping,special):
		'''create pizza object and add into cart'''
		pizza = Pizza(size,topping,special)
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