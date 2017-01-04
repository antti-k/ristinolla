import unittest

from risti import emptyBoard

class TestiLuokka(unittest.TestCase):
	def testEmptyBoard(self):
		self.assertEqual(emptyBoard(3, 3), [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
		self.assertEqual(emptyBoard(4, 5), [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

	

unittest.main()

