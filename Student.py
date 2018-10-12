class Student:

	def __init__(self, firstname, lastname, telephone):
		self.firstname = firstname
		self.lastname = lastname
		self.email = None
		self.grade = None
		self.telephones = []
		self.telephones.append(telephone)

	def add_email(self, email):
		self.email = email
		print("Email has been added for " + self.firstname)

	def add_grade(self, grade):
		self.grade = grade
		print("Grade has been entered for " + self.firstname)

	def add_number(self, number, numbertype):
		self.telephones.append(Telephone(number, numbertype))
		print("Phonenumber has been added for " + self.firstname)

	def __str__(self):
		res = 'Firstname: ' + self.firstname + '\nLastname: ' + self.lastname
		if self.email != None:
			res = res + '\nEmail: ' + self.email

		if self.grade != None:
			res = res + '\n' + 'Grade: ' + self.grade

		for n in self.telephones:
			res = res + str(n)

		return res
    	
	def name(self):
		return 'Name: ' + self.firstname + ' ' + self.lastname

class Telephone:

	def __init__(self, number, numbertype):
		self.number = number
		self.numbertype = numbertype


	def __str__(self):
		return '\n' + str(self.numbertype) +': ' + str(self.number)
    
loa = Student('Loa', 'Marx', Telephone('0157 72479996', 'mobile'))
loa.add_email('loaleemarx@gmail.com')
loa.add_number('05505 509433', 'home')

print(str(loa))

