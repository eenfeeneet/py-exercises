class Student(object):
	""""""
	def __init__ (self, firstName, lastName, age, index):
		self._firstName = firstName
		self._lastName = lastName
		self._age = age
		self._email = firstName + "." + lastName + "@raceisamazing.com.sg"
		self._index = index
		self._fullName = firstName + " " + lastName

	def __str__ (self):
		return "name: {}, email: {} ".format(self._firstName,self._email)

	def GetFullName(self): #put a self in the args for it to be a instance class method
		return (self._firstName + " " + self._lastName) #have to be .self to refer to the instance property

def main():
	student1 = Student("ethan","chen","32","2")
	a = student1
	print (a)
	print(student1._fullName)
	print(student1._email)
	print(student1.GetFullName())
	# print(Student.__dict__) #identify all properties in the class

if __name__ == '__main__':
	main()