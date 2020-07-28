#Chrystian Melo
from random import randrange


matSize = 3


class Jogador:
	def __init__(self,mode, symbol):
		self.mode = mode#1 -> player   0-> bot
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
				if (equal == matSize):# Won  horizontally 
					return hor
		#vertical
		for j in range(0,matSize):#column
			equal = 0
			ver = self.matrix[0][j]
			if (ver != " "):
				for i in range(0,matSize):#line
					if(self.matrix[i][j] == ver):
						equal+=1
				if (equal == matSize):#Won  vertically 
					return ver
		return False

	def getEmptyPositions(self):#whe
		amount = 0
		for i in range(0,matSize):
			for j in range(0,matSize):
				if (self.matrix[i][j] == " "):
					amount+=1
		return amount

	def setPositionFilled(self,position):
		for i in range(0,matSize):
			for j in range(0,matSize):
				if (self.matrix[i][j] == " "):
					position-=1
					if(position == 0):
						return [i,j]

	def printMat(self):
		print("Tabuleiro")
		top = ""
		for i in range(0,matSize):#making title
			top += "    " + str(i+1)
		print(top)#title
		for i in range(0,matSize):
			print(i+1,self.matrix[i])#lineIndicator + elements
		print()


def random(number):#quantity
	return randrange(1,number)

def botPlay():
	where  = game.getEmptyPositions()
	if(where != 0):
		if (where != 1):
			position = game.setPositionFilled(random(where))
		elif (where == 1):
			position = game.setPositionFilled(1)
		return position


#main

game = Tabuleiro()

#menu[start]
print("\n\t\t\t\t\tJogo da Velha"+
	  "\n\t\t\t\tDesenvolvido por Chrystian Melo"+
	  "\n\t\tEste jogo consiste em um tabuleiro dividido em uma matriz 3x3 com linhas de 1 a 3 e colunas 1 a 3."+
	  "\n\t\tPara jogar, após jogador selecionado('X' ou 'O'), indique o numero da linha e, em seguida, o numero da coluna onde pretende marcar.")
print("Digite apenas o numero referente a sua resposta.:")
done=0
while(done == 0):
	try:
	    answ = int(input("Opções de jogo.:\n\t1)BotxBot(digite 1)\n\t2)PlayerxPlayer(digite 2)\n\t3)PlayerxBot(digite 3)\n"))
	    done = 1
	except ValueError:
	    print("Oops! Digite apenas numeros.")
	    done = 0
	if(done ==1 and answ != 1 and answ != 2 and answ != 3):
	    print("Oops! Digite apenas (1, 2 ou 3)")
	    done = 0
	elif(done == 1 and answ == 1):#botxbot
		print("Player 1.: X \nPlayer2.: O")
		player1 = Jogador(0,"X")
		player2 = Jogador(0,"O")
	elif(done == 1 and answ == 3):#playerxbot
		done2 = 0
		while(done2 == 0):
			try:
			    answ = int(input("Você deseja jogar com X(digite 1) ou O(digite 2)"))
			    done2 = 1
			except ValueError:
			    print("Oops! Digite apenas numeros.")
			    done2 = 0
			if(done2 ==1 and answ != 1 and answ != 2):
			    print("Oops! Digite apenas (1 ou 2)")
			    done2= 0
		if(answ == 1):#player selected "x"
			player1 = Jogador(1,"X")
			player2 = Jogador(0,"O")
		else:#player selected "o"
			player2 = Jogador(1,"O")
			player1 = Jogador(0,"X")
	elif(done == 1 and answ == 2):#playerxplayer
		print("Jogador 1 escolha seu simbolo.:")
		done2 = 0
		while(done2 == 0):
			try:
			    answ = int(input("Você deseja jogar com X(digite 1) ou O(digite 2)"))
			    done2 = 1
			except ValueError:
			    print("Oops! Digite apenas numeros.")
			    done2 = 0
			if(done2 ==1 and answ != 1 and answ != 2):
			    print("Oops! Digite apenas (1 ou 2)")
			    done2= 0
		if(answ == 1):#player selected "x"
			player1 = Jogador(1,"X")
			player2 = Jogador(1,"O")
		else:#player selected "o"
			player2 = Jogador(1,"O")
			player1 = Jogador(1,"X")
#menu[end]

player = 1
finished = 0
while(game.getEmptyPositions() != 0 and finished == 0):
	game.printMat()
	if (player == 1):#player1
		print("Proximo jogador ("+player1.symbol+")")
		if(player1.mode == 1):#player
			print("Sobre seu proximo movimento.:(use as coordenadas indicadas no tabuleiro de linha e coluna)")
			done = 0
			while(done == 0):
				try:
				    line = int(input("Qual linha?"))-1#start from 0, so less to use
				    column = int(input("Qual coluna?"))-1#start from 0, so less to use
				    done = 1
				except ValueError:
				    print("Oops! Digite apenas numeros.")
				    done = 0
				if(done == 1 and game.checkEmpty(line,column) == False):
					print("Oops! Esse local já foi preenchido. Tente novamente.")
					done = 0
			player1.play(game.matrix,line,column)
		else:
			position = botPlay()
			player1.play(game.matrix,position[0],position[1])
		player = 2
	else:#player2
		print("Proximo jogador ("+player2.symbol+")")
		if(player2.mode == 1):#player
			print("Sobre seu proximo movimento.:(use as coordenadas indicadas no tabuleiro de linha e coluna)")
			done = 0
			while(done == 0):
				try:
				    line = int(input("Qual linha?"))-1#start from 0, so less to use
				    column = int(input("Qual coluna?"))-1#start from 0, so less to use
				    done = 1
				except ValueError:
				    print("Oops! Digite apenas numeros.")
				    done = 0
				if(done == 1 and game.checkEmpty(line,column) == False):
					print("Oops! Esse local já foi preenchido. Tente novamente.")
					done = 0
			player2.play(game.matrix,line,column)
		else:
			position = botPlay()
			player2.play(game.matrix,position[0],position[1])
		player =1

	if(game.checkVictory() != False):#checking if it can be played
		finished = 1

game.printMat()#final state

if(game.checkVictory() == False):
	print("Deu empate!!")
elif(game.checkVictory() == player1.symbol):
	print("Player 1 venceu ("+player1.symbol+")!!")
else:
	print("Player 2 venceu ("+player2.symbol+")!!")