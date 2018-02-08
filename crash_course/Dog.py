class Dog(object):
	""" Modeling a dog """
	
	def __init__(self,name,age):
		""" Init name and age attributes """
		self.name = name
		self.age = age
		
	def sit(self):
		""" Simulate a dog sitting """
		print (self.name.title() + " is now sitting.")
		
	def roll_over(self):
		""" Simulte a dog rolling over """
		print (self.name.title() + " rolled over!")
		

