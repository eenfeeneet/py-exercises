class drinks:
	def __init__(self,temp,sugar,cream):
		self._temp = temp
		self._sugar = sugar
		self._cream = cream
		self._cost = self.cost()
	def __str__(self):
		return "Here is your {} drink with {} and {}. It cost {}".format(self._temp,self._sugar,self._cream,self._cost)

	def cost(self):
		cost = 1
		if self._temp == "Hot":
			cost += 0.3
		if self._sugar == "More sugar":
			cost += 0.2
		if self._cream == "More cream":
			cost += 0.1
		return round(cost,2)

class payment:
	def __init__(self,mode):
		self._mode = mode

class cash(payment):
	def __init__(self,mode,payment,change):
		payment.__init__(mode)
		self._payment = payment
		self._change = change
	def __str__(self):
		return "you have paid ${} and here is your change of ${}".format(self._payment,self._change)

temp = ""
sugar = ""
cream = ""

def main():
	if OrderDrink() == True:
		buyDrink()

def buyDrink():
	ChooseTemp()
	ChooseSugar()
	ChooseCream()
	drinkObj = drinks(temp,sugar,cream)
	print(drinkObj)

	if PaymentMode() == True:
		payment = float(input("please enter amount you are paying: "))
		change = round(payment - drinkObj._cost,2)
		cashPaymentObj = cash("cash",payment,change)
		print(cashPaymentObj)
	else:
		print("you have successfully paid via a cashless method")

def OrderDrink():
	selection = str (input("would you like to order a drink? "))
	if selection.lower() == "y":
		return True
	elif selection.lower() == "n":
		return False

def ChooseTemp():
	selection = str (input("choose a hot or cold drink: "))
	global temp
	if selection.lower() == "hot":
		temp = "Hot"
	elif selection.lower() == "cold":
		temp = "Cold"

def ChooseSugar():
	selection = str (input("choose more or less sugar: "))
	global sugar
	if selection.lower() == "more":
		sugar = "More sugar"
	elif selection.lower() == "less":
		sugar = "Less sugar"

def ChooseCream():
	selection = str (input("choose more or less cream: "))
	global cream
	if selection.lower() == "more":
		cream = "More cream"
	elif selection.lower() == "less":
		cream = "Less cream"

def PaymentMode():
	selection = str(input("choose cash or cashless payment: "))
	if selection.lower() == "cash":
		return True
	elif selection.lower() == "cashless":
		return False

if __name__ == '__main__':
	main()
