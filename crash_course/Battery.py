class Battery(object):
	""" Simple battery class for an electric car """
	def __init__ (self, battery_size=70):
		""" Initialize the battery_size variable """
		self.battery_size = battery_size
		
	def describe_battery(self):
		""" Prints a statement describing the battery """
		print ("This car has a " + str(self.battery_size) + "-kWh battery.")
		
	def get_range(self):
		""" Print a statement about the range (in miles) of the car with this battery """
		
		if self.battery_size == 70:
			battery_range = 240
		elif self.battery_size == 85:
			battery_range = 270
			
		message = "This car can go approximately " + str(battery_range)
		message += " miles on a full charge."
		
		print message
		
	def upgrade_battery(self):
		""" If the battery size isn't 85, make it 85 """
		if self.battery_size != 85:
			self.battery_size = 85
		
