import random

class Die(object):
	""" Implements a simple dice object """
	
	def __init__(self, sides=6):
		""" Initializes sides to a default value if one isn't provided """
		self.sides = sides
	
	def roll_die(self):
		""" Returns a random number 1 and the number of sides """
		return random.randint(1, self.sides)
		

