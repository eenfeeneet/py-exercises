from Tkinter import*

class Window(object):

	def __init__(self,master):
		self.master = master
		self.sizeInput = StringVar()
		self.toppingInput = StringVar()

		master.title('pizzahut')
		master.geometry('600x400')
		master.resizable(width=False,height=False)

		master.grid_rowconfigure(1,weight=1)
		master.grid_columnconfigure(1,weight=1)

		self.leftFrame = Frame(master,width = 200, height = 400)
		self.leftFrame.grid(row = 0,column=0)
		self.rightFrame = Frame(master,width = 400, height = 400)
		self.rightFrame.grid(row = 0,column = 1)

		self.r1 = Radiobutton(self.leftFrame,text = 'small',variable=self.sizeInput, value='small').grid(row=0)
		self.r2 = Radiobutton(self.leftFrame, text = 'medium', variable = self.sizeInput, value = 'medium').grid(row=1)
		self.r3 = Radiobutton(self.leftFrame, text = 'beef',variable = self.toppingInput, value = 'beef').grid(row=2)
		self.r4 = Radiobutton(self.leftFrame, text = 'clam',variable = self.toppingInput, value = 'clam').grid(row=3)
		self.buttonAdd = Button(self.leftFrame, text = 'ADD', command= self.AddListBox)
		self.buttonAdd.grid(row=4)
		self.listBox = Listbox(self.leftFrame) #has to be written this way or it wont work
		self.listBox.grid(row=5)
		self.totalPriceLabelOutput = Label(self.leftFrame) #has to be written this way or it wont work
		self.totalPriceLabelOutput.grid(row =6)
		self.buttonRemove = Button(self.leftFrame, text = 'REMOVE', command= self.RemoveListBox)
		self.buttonRemove.grid(row=7)

		self.canvas = Canvas(self.rightFrame,width=400,height=400,bg="white").pack()

	def AddListBox(self):

		Pizza.AddPizza(self.sizeInput.get(),self.toppingInput.get())
		self.listBox.insert(END,'{} {} pizza : ${}'.format(Pizza.cart[-1].size,Pizza.cart[-1].topping,Pizza.cart[-1].price))
		self.UpDateTotalPrice()
		
	def RemoveListBox(self):
		sel = self.listBox.curselection() #this is return a list of indexes
		self.listBox.delete(sel)
		intsel = sel[0]
		Pizza.RemovePizza(intsel)
		self.UpDateTotalPrice()

	def UpDateTotalPrice(self):
		totalPrice = 0
		for index in range (0, len(Pizza.cart)):
			totalPrice = totalPrice + Pizza.cart[index].price
		self.totalPriceLabelOutput.config(text = 'total price:${}'.format(totalPrice))

class Pizza(object):

	ingredients = {'small':5,'medium':10,'big':20,'beef':5,'cheese':3,'clam':3}
	cart =[]  #class attribute that stores list of added objects

	def __init__(self,size,topping):
		self.size = size
		self.topping = topping
		price1= self.ingredients.get(size)
		price2= self.ingredients.get(topping)
		self.price = price1 + price2

	def __str__(self):
		return '{} {} :${}'.format(self.size,self.topping,self.price)
	#throwback from w indow class
	@classmethod
	def AddPizza(cls,size,topping):
		'''create pizza object and add into cart'''
		pizza = Pizza(size,topping)
		cls.cart.append(pizza)

	@classmethod
	def RemovePizza(cls,sel):
		cls.cart.pop(sel) #remove pizza object by index. sel from listbox is the same index as items[]

def main():
	# Pizza.AddPizza('small','beef')
	# Pizza.AddPizza('medium','cheese')
	# Pizza.AddPizza('big', 'beef')
	# for index in range (0,len(Pizza.cart)):
	# 	print(Pizza.cart[index])
	# for item in Pizza.cart:
	# 	Pizza.costTotal.append(item.price)
	# print ('total sum of pizzas = ${}'.format(sum(Pizza.costTotal)))

	root= Tk()
	window = Window(root)
	root.mainloop()

if __name__ == '__main__':
	main()