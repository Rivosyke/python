#!/usr/bin/python

class Calculator:
	def __init__(self, inA, inB):
		self.a = inA
		self.b = inB
		
	def add(self):
		return self.a + self.b
		
	def multiply(self):
		return self.a * self.b

class ScienceCalc (Calculator):
	def power(self):
		return pow(self.a, self.b)

class Calculator_input:
#	def __init__(self):		
	def add(self, inA, inB):
		return inA + inB
		
	def multiply(self, inA, inB):
		return inA * inB

class ScienceCalc_input (Calculator_input):
	def power(self, inA, inB):
		return pow(inA, inB)

def quickAdd (a,b):
	return a+b
