def emptyBoard(x, y):
	tmp1 = []
	for i in range(y):
		tmp2 = []
		for j in range(x):
			tmp2.append(0)
		tmp1.append(tmp2)
	return tmp1

def markBoard(x, y, board, player):
	if board[y][x] == 0:
		tmpboard = board
		tmpboard[y][x] = player
		return tmpboard
	else:
		return False

def clearBoard(board):
	tmbpboard = board
	for i in range(len(tmpboard)):
		for j in range(len(tmpboard[i])):
			tmpboard[i][j] = 0
	return tmpboard

	
