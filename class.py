#!/usr/bin/python

class Calculator:
	def __init__(self):
		self = self
		
	def add(self, inA, inB):
		return inA + inB
		
	def multiply(self, inA, inB):
		return inA * inB

class ScienceCalc (Calculator):
	def power(self, inA, inB):
		return pow(inA, inB)


newCalc = Calculator()
sciCalc = ScienceCalc()

print newCalc.add(2,6)
print newCalc.multiply(5,10)
print sciCalc.power(2,3)


