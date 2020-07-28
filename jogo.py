#Chrystian Melo
from random import randrange

class Jogador:
	def __init__(self, mode, symbol):
		self.mode = mode#1->pc, 2-> player 
		self.symbol = symbol#1 -> "X" or 2 -> "O

class Tabuleiro:
	matrix = [[0]*3 for i in range(3)]#0 -> empty | 1 -> "X" | 2 -> "O"
	def play(self,symbol,i,j):#Jogador(),row,column
		if(self.matrix[i][j] == 0):
			self.matrix[i][j] = symbol
		#else: error = "already filled"

def getEmptyPositions(matrix):
	amount = 0
	for i in range(0,3):
		for j in range(0,3):
			if (matrix[i][j] == 0):
				amount+=1
	return amount

def setPositionFilled(matrix,position):
	for i in range(0,3):
		for j in range(0,3):
			if (matrix[i][j] == 0):
				position-=1
				if(position == 0):
					return [i,j]

def random(number):#quantity
	return randrange(1,number)

def printMat(matrix):
	print("Tabuleiro")
	for i in range(0,3):
		print(matrix[i])

def botPlay(symbol):
	where  = getEmptyPositions(game.matrix)
	if(where != 0):
		if (where != 1):
			position = setPositionFilled(game.matrix,random(where))
		elif (where == 1):
			position = setPositionFilled(game.matrix,1)
		game.play(symbol,position[0],position[1])

#def checkVictory(matrix)


player1 = Jogador(1,"X")
player2 = Jogador(1,"Y")

game = Tabuleiro()

player = 1
while(getEmptyPositions(game.matrix) != 0):
	printMat(game.matrix)
	if (player == 1):
		botPlay(player1.symbol)
		player = 2
	else: 
		botPlay(player2.symbol)
		player = 1

printMat(game.matrix)
