#!/usr/bin/python

import unittest

from Employee import Employee

class TestEmployee(unittest.TestCase):
	def setUp(self):
		self.bob = Employee("Bob", "Barker", 90000)
		
	def test_give_default_raise(self):
		self.bob.give_raise()
		self.assertEqual(95000, self.bob.salary)
	def test_give_custom_raise(self):
		self.bob.give_raise(10000)
		self.assertEqual(100000, self.bob.salary)
unittest.main()
