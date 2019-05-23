import unittest
from TestlinkRunner import TestLinkRunner
class demonstratingTLRunner(unittest.TestCase):
    def test_20_TestPass(self):
        pass
    
    def test_23_TestFailure(self):
        self.fail("test fail")
def add(num1,num2):
	return num1+num2
def mul(num1,num2):
	return num1*num2
def sub(num1,num2):
	return num1-num2
def test_add():
	assert add(1,2)==3
def test_mul():
	assert mul(3,4)==12
def test_sub():
	assert sub(3,3)==0
