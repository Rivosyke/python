#!/usr/bin/python

from Dog import Dog
from Car import Car, ElectricCar
from Die import Die

my_new_car = Car('audi', 'a4', 2016)

print (my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', '2013')
my_used_car.update_odometer(23000)
my_used_car.increment_odometer(100)
my_used_car.read_odometer()


my_tesla = ElectricCar('tesla', 'model s', 2016)

print (my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()


six_sided = Die()
print "\n----- Start Six Sided Die Rolls -----"
for x in range(1,10):
	print str(six_sided.roll_die())


ten_sided = Die(10)
print "\n----- Start Ten Sided Die Rolls -----"	
for x in range(1,10):
	print str(ten_sided.roll_die())

twenty_sided = Die(20)
print "\n----- Start Twenty Sided Die Rolls -----"	
for x in range(1,10):
	print str(twenty_sided.roll_die())

