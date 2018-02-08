class Car(object):
	""" A simple car """
	
	def __init__(self, make, model, year):
		""" Initialize attributes to describe a car """
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name (self):
		""" Return a nearly formatted descriptive name """
		long_name = str(self.year) + ' ' + self.make + " " + self.model
		return long_name.title()
		
	def read_odometer(self):
		""" Print a statement showing the car's odometer reading """
		print ("This car has " + str(self.odometer_reading) + " miles on it.")
	
	def update_odometer(self, mileage):
		""" Set the odometer reading to the value of mileage """
		
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print "You can't subtract miles on a car!"
	
	def increment_odometer (self, miles):
		""" Increments the current odometer value with the value of miles """
		if miles >= 0:
			self.odometer_reading += miles
		else:
			print "You can't add negative miles to the odometer!"
		
		
	
	
