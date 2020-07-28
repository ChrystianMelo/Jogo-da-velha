#Chrystian Melo
from random import randrange

matSize = 3

class Jogador:
	def __init__(self, symbol):
		self.symbol = symbol#1 -> "X" or 2 -> "O
	def play(self,matrix,i,j):#Jogador(),row,column
		if(matrix[i][j] == " "):
			matrix[i][j] = self.symbol
			return True
		else: 
			return False #error = "already filled"

class Tabuleiro:
	matrix = [[" "]*matSize for i in range(matSize)]#0 -> empty | 1 -> "X" | 2 -> "O"

	def checkEmpty(self,line,column):
		if(self.matrix[line][column] == " "):
			return True
		return False

	def checkVictory(self):
		#diagonal(TOP-BOTTOM)
		diag = self.matrix[0][0]
		equal = 0
		if (diag != " "):
			for i in range(0, matSize):#line
				if(self.matrix[i][i] == diag):#diag -> where line = column
					equal+=1
			if (equal == matSize):#diagonal filled
				return diag
		#diagonal(BOTTOM-TOP)
		equal = 0
		diag2 = self.matrix[0][matSize-1]
		if (diag2 != " "):
			for i in range(0, matSize):#line
				if(self.matrix[i][matSize-1-i] == diag2):#sum(line,column) = matSize-1
					equal+=1
			if (equal == matSize):#diagonal filled
				return diag2
		#horizontal
		for i in range(0,matSize):#line
			equal = 0
			hor = self.matrix[i][0]
			if (hor != " "):
				for j in range(0,matSize):#column
					if(self.matrix[i][j] == hor):
						equal+=1
				if (equal == matSize):# Ganhou  horizontally 
					return hor
		#vertical
		for j in range(0,matSize):#column
			equal = 0
			ver = self.matrix[0][j]
			if (ver != " "):
				for i in range(0,matSize):#line
					if(self.matrix[i][j] == ver):
						equal+=1
				if (equal == matSize):# Ganhou  vertically 
					return ver
		return False

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
	top = ""
	for i in range(0,matSize):#making title
		top += "    " + str(i+1)
	print(top)#title
	for i in range(0,matSize):
		print(i+1,matrix[i])#lineIndicator + elements
	print()

def botPlay():
	where  = getEmptyPositions(game.matrix)
	if(where != 0):
		if (where != 1):
			position = setPositionFilled(game.matrix,random(where))
		elif (where == 1):
			position = setPositionFilled(game.matrix,1)
		return position


game = Tabuleiro()

print("\n\t\t\t\t\tJogo da Velha"+
	  "\n\t\t\t\tDeveloped by Chrystian Melo")
print("Digite apenas o numero referente a sua resposta.:")
done = 0
while(done == 0):
	try:
	    answ = int(input("Você deseja jogar com X(digite um) ou O(digite dois)"))
	    done = 1
	except ValueError:
	    print("Oops! That's not a valid option. Only integers")
	    done = 0
	if(done ==1 and answ != 1 and answ != 2):
	    print("Oops! That's not a valid option. Only integers(1 or 2)")
	    done = 0
if(answ == 1):
	player1 = Jogador("X")
	player2 = Jogador("O")
else:
	player1 = Jogador("O")
	player2 = Jogador("X")


player = 1
finished = 0
while(getEmptyPositions(game.matrix) != 0 and finished == 0):
	printMat(game.matrix)
	if (player == 1):#player playing
		print("Sobre seu proximo movimento.:(use as coordenadas indicadas no tabuleiro de linha e coluna)")
		done = 0
		while(done == 0):
			try:
			    line = int(input("Qual linha?"))-1#start from 0, so less to use
			    column = int(input("Qual coluna?"))-1#start from 0, so less to use
			    done = 1
			except ValueError:
			    print("Oops! That's not a valid option. Only integers")
			    done = 0
			if(done == 1 and game.checkEmpty(line,column) == False):
				print("Oops! Esse local já foi preenchido. Tente novamente.")
				done = 0
		player1.play(game.matrix,line,column)
		player = 2
	else:#bot playing
		position = botPlay()
		player2.play(game.matrix,position[0],position[1])
		player = 1

	if(game.checkVictory() != False):#checking if it can be played
		finished = 1


printMat(game.matrix)#final state

if(game.checkVictory() == False):
	print("Deu empate")
elif(game.checkVictory() == player1.symbol):
	print("Você ganhou!!")
else:
	print("Você perdeu!! Tente novamente...")