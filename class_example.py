class Person(object):
	legs = 2
	def __init__(self, firstName, lastName):
		self._firstName = firstName
		self._lastName = lastName

	def __str__(self):
		return "{} {}".format(self._firstName, self._lastName)

	@staticmethod
	def MakeSound():
		print ("hello")

class Developer(Person):
	def __init__(self,firstName,lastName):
		super().__init__(firstName,lastName)
		self._progLang = "python"

	def __str__(self):
		return super().__str__() + " is a developer and knows {}".format(self._progLang)

def main():
	person1 = Person("ethan","chen")
	devperson1 = Developer("ethan", "chen")
	print (person1)
	print (devperson1)
	print (devperson1._progLang)
	person1.MakeSound()

if __name__ == '__main__':
	main()