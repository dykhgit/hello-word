# coding=utf8
import unittest
import sys
sys.path.append("..")

from src.aw import *

class TestAw(unittest.TestCase):

	def test_simulate(self):
		result=simulate(10000)
		self.assertLess(result, 0.6)
		self.assertGreater(result, 0.4)
	

if __name__=="__main__":
	unittest.main()
