class someFunction(object):

	def __init__(self):
		self.someATT = "wonderful"

	def function1(self):
		print(self.someATT)

	@classmethod
	def classfunction(cls):
		print(cls.someATT)

	@staticmethod
	def staticfunction():
		G1 = someFunction()
		print(G1.someATT)

class Person(object):
	def __init__ (self,name,balance):
		self._name = name
		self._balance = balance


	def Withdraw(self,amount):
		self._balance -= amount
		return self._balance

def main():
	person1 = Person("ethan",5000)
	print(person1._name)
	person1.Withdraw(1000)
	print(person1._balance)

if __name__ == '__main__':
			main()		