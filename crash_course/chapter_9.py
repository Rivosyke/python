#!/usr/bin/python

from Dog import Dog
from Car import Car, ElectricCar

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
my_tesla.describe_battery()
