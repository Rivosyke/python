#!/usr/bin/python



class Test (object):
	Test.class_var_1 = "test_class"
	
	def __init__ (self, x):
		self.a = x
	
	
newTestA = Test(2)
Test.tester = "a_test"
newTestB = Test(3)

print newTestA.a
print newTestB.a
print newTestA.class_var_1
print newTestB.class_var_1
print "**********************************\n"

print newTestB.tester
newTestA.class_var_1 = "not_test"
Test.class_var_1 = "second_test"
print newTestA.class_var_1
print newTestB.class_var_1
