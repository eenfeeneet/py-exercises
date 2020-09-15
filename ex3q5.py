class pizza:
	def __init__(self,size,crust,ingredient):

		if size.lower() == "s": 
			self.size = "small"
		elif size.lower() == "m":	
			self.size = "medium"
		elif size.lower() == "l":	
			self.size = "large"
		self.crust = crust
		self.ingredient = ingredient

	def __str__(self):
		return "you have ordered a {} pizza with {} for ingredients".format(self.size,self.ingredient)

class magerita(pizza):

	def __init__(self,size,crust,ingredient):
		super(magerita,self).__init__(size,crust,ingredient)
		self.ingredient = ingredient + " " + "garlic" + " " + "olive oil" #default ingredients to include garlic & olive oil

	def addToppings(self, *args):
		for x in args:
			self.ingredient = self.ingredient + " " + x
		return self.ingredient
		
	def __str__(self):
		return "you have ordered a {} magerita pizza with {} for ingredients.".format(self.size,self.ingredient)

def main():
	pizza1 = pizza("L","Thin","chicken") #declare size as caps to test .lower func
	print (pizza1.crust) #check crust
	print (pizza1.size) #check size
	pizza2 = magerita("L","Thick","beef")
	pizza2.addToppings("cheese","capsicum")
	print(pizza2)

if __name__ == '__main__':
	main()