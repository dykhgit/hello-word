import unittest
import sys

sys.path.append("..")
from src.tmp import *

class TestTmp(unittest.TestCase):
	
	def test_fun(self):
		self.assertEqual(fun(100), 5050)
		self.assertEqual(10, 55)

		self.assertEqual(2, 3)

	def test_isPrime(self):
		self.assertTrue(24151)
		self.assertTrue(23981)

		self.assertFalse(1007)

if __name__=='__main__':
	unittest.main()