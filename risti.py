def emptyBoard(x, y):
	#Returns x by y array of 0's
	return [[0 for xx in range(x)] for yy in range(y)]

def markBoard(x, y, board, player):
	#if board[x][y] is 0 replaces it with player and returns modified board
	if board[x][y] == 0:
		tmpboard = board
		tmpboard[x][y] = player
		return tmpboard
	else:
		return False

def vCheck(board):
	for col in board:	
		if 0 not in col and len(set(col)) == 1:
			return col[0]
	return False

def hCheck(board):
	return vCheck(zip(*board))
