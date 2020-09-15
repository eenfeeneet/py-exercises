class Pizza(object):
	def __init__(self,size,topping):
		self.size = size
		self.topping = topping
		price1= Ingredient.items.get(size)
		price2= Ingredient.items.get(topping)
		self.price = price1 + price2

class Ingredient(object):
	items = {'small':5,'medium':10,'big':20,'beef':5,'cheese':3,'clam':3} #class attribute that stores list of ingredients and cost

class Cart(object):
	items =[]  #class attribute that stores list of added objects
	costTotal = []

	#throwback from w indow class
	@classmethod
	def addPizza(cls,size,topping):
		cls.items.append(Pizza(size,topping)) #create Pizza object and add into cart
	@classmethod
	def removePizza(cls,sel):
		cls.items.pop(sel) #remove pizza object by index. sel from listbox is the same index as items[]

def main():

	Cart.addPizza('small','cheese') #created objects from button pressed
	Cart.addPizza('medium','beef')
	Cart.addPizza('big','clam')
	Cart.removePizza(1)

	for item in Cart.items:
		Cart.costTotal.append(item.price)
	print ('total sum of pizzas = ${}'.format(sum(Cart.costTotal)))
	for index in range(0,len(Cart.items)):
		print('{} {} pizza = ${}'.format(Cart.items[index].size,Cart.items[index].topping,Cart.items[index].price))


if __name__ == '__main__':
	main()