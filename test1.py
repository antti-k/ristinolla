import unittest

from risti import emptyBoard
from risti import markBoard
from risti import vCheck
from risti import hCheck

class TestiLuokka(unittest.TestCase):
	def testEmptyBoard(self):
		self.assertEqual(emptyBoard(3, 3), [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
		self.assertEqual(emptyBoard(4, 5), [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

	def testMarkBoard(self):
		board1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
		board2 = [[0, 0, 0], [0, 0, 1], [0, 0, 0]]
		self.assertEqual(markBoard(1, 2, board1, 1), board2)

	
	def testVCheck(self):
		board = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
		self.assertEqual(vCheck(board), 1)
		board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
		self.assertEqual(vCheck(board), False)

	def testHCheck(self):
		board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
		self.assertEqual(hCheck(board), False)
		board = [[0, 2, 0], [0, 2, 0], [0, 2, 0]]
		self.assertEqual(hCheck(board), 2)	

	


unittest.main()
