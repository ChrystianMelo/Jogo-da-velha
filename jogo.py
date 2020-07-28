#Chrystian Melo
from random import randrange

matSize = 3

class Jogador:
	def __init__(self, mode, symbol):
		self.mode = mode#1->pc, 2-> player 
		self.symbol = symbol#1 -> "X" or 2 -> "O

class Tabuleiro:
	matrix = [[" "]*matSize for i in range(matSize)]#0 -> empty | 1 -> "X" | 2 -> "O"
	def play(self,symbol,i,j):#Jogador(),row,column
		if(self.matrix[i][j] == " "):
			self.matrix[i][j] = symbol
		#else: error = "already filled"

def getEmptyPositions(matrix):
	amount = 0
	for i in range(0,matSize):
		for j in range(0,matSize):
			if (matrix[i][j] == " "):
				amount+=1
	return amount

def setPositionFilled(matrix,position):
	for i in range(0,matSize):
		for j in range(0,matSize):
			if (matrix[i][j] == " "):
				position-=1
				if(position == 0):
					return [i,j]

def random(number):#quantity
	return randrange(1,number)

def printMat(matrix):
	print("Tabuleiro")
	for i in range(0,matSize):
		print(matrix[i])

def botPlay(symbol):
	where  = getEmptyPositions(game.matrix)
	if(where != 0):
		if (where != 1):
			position = setPositionFilled(game.matrix,random(where))
		elif (where == 1):
			position = setPositionFilled(game.matrix,1)
		game.play(symbol,position[0],position[1])

def checkVictory(matrix):
	#diagonal(TOP-BOTTOM)
	diag = matrix[0][0]
	equal = 0
	if (diag != " "):
		for i in range(0, matSize):#line
			if(matrix[i][i] == diag):#diag -> where line = column
				equal+=1
		if (equal == matSize):#diagonal filled
			return diag +"Won"
	#diagonal(BOTTOM-TOP)
	equal = 0
	diag2 = matrix[0][matSize-1]
	if (diag2 != " "):
		for i in range(0, matSize):#line
			if(matrix[i][matSize-1-i] == diag2):#sum(line,column) = matSize-1
				equal+=1
		if (equal == matSize):#diagonal filled
			return diag2 +"Won"
	#horizontal
	for i in range(0,matSize):#line
		equal = 0
		hor = matrix[i][0]
		if (hor != " "):
			for j in range(0,matSize):#column
				if(matrix[i][j] == hor):
					equal+=1
			if (equal == matSize):#won horizontally 
				return hor +"Won"
	#vertical
	for j in range(0,matSize):#column
		equal = 0
		ver = matrix[0][j]
		if (ver != " "):
			for i in range(0,matSize):#line
				if(matrix[i][j] == ver):
					equal+=1
			if (equal == matSize):#won vertically 
				return ver +"Won"
	return False

player1 = Jogador(1,"X")
player2 = Jogador(1,"O")

game = Tabuleiro()

player = 1
finished = 0
while(getEmptyPositions(game.matrix) != 0 and finished == 0):
	printMat(game.matrix)
	if (player == 1):
		botPlay(player1.symbol)
		player = 2
	else: 
		botPlay(player2.symbol)
		player = 1

	if(checkVictory(game.matrix) != False):
		finished = 1

printMat(game.matrix)
print(checkVictory(game.matrix))
