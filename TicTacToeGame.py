#Welcome to the inventors and Innovations team's Tic-tac-toe game!

#Authors: Sai Gutala, Nicholas Paschke, Shruti Gupta

#This game was written in python and is encouraged to customize, 

#Possible modifications to this game:
#Challenge 1: How could you make it print your name after you win?
#Challenge 2: Could you prompt the user to play again if they would so desire? 
#Challenge 3: Could you do in less lines in python?
#Challenge 4: Can you fix the bug which allows you to play a place which has already been played? 
#Challenge 5: Could you make the perfect tic-tac-toe AI?
#Challenge 6: Could you do this in a GUI and clickable tiles?


#This board makes this game awfully weird to iterate through... could you do it in less lines?
Board = [['1','2','3'],['4','5','6'],['7','8','9']]

#This function prints out the board
def print_board():
	for i in range(0,3,1):
		for j in range(0,3,1):
			print(''+Board[i][j]+'|',end='')
		print(end='\n')
		if (i < 2):
			print('-'*8)

#This function essentially checks if the board already has a winner on it.
def check_winner():
	#Checking horizontals
	for i in range(0,3,1):
		if (Board[i][0] == Board[i][1] and Board[i][1] == Board[i][2]):
			if (Board[i][0] == 'X'):
				print('X is the winner!!!')
			else:
				print('O is the winner!!!')
			return True
	#Checking verticals 
		if (Board[0][i] == Board[1][i] and Board[1][i] == Board[2][i]):
			if (Board[0][i] == 'X'):
				print('X is the winner!!!')
			else:
				print('O is the winner!!!')
			return True
	#Checking diagonals 
	#This is possibly a line you could make more efficiently in challenge 3! (Hint: Palondromes)
	if (Board[0][0] == Board[1][1] and Board[2][2] == Board[1][1] or Board[0][2] == Board[1][1] and Board[1][1] == Board[2][0]):
		if (Board[0][0] == 'X'):
			print('X is the winner!!!')
		else:
			print('O is the winner!!!')
		return True

	return False

#This is where the game is played 
def Game():
	#Challenge 1 would start here!
	

	X = 11
	O = 11

	while(check_winner() == False):
		print_board()
		while(X < 0 or X > 10):
			X = int(input('X, type the number you would like to place an X down in: '))
		#Here's a great challenge for challenge 3!
		if (X == 1 and Board[0][0] == '1'):
			Board[0][0] = 'X'
		elif(X == 2 and Board[0][1] == '2'):
			Board[0][1] = 'X'
		elif(X == 3 and Board[0][2] == '3'):
			Board[0][2] = 'X'
		elif(X == 4 and Board[1][0] == '4'):
			Board[1][0] = 'X'
		elif(X == 5 and Board[1][1] == '5'):
			Board[1][1] = 'X'
		elif(X == 6 and Board[1][2] == '6'):
			Board[1][2] = 'X'
		if (X == 7 and Board[2][0] == '7'):
			Board[2][0] = 'X'
		elif(X == 8 and Board[2][1] == '8'):
			Board[2][1] = 'X'
		elif(X == 9 and Board[2][2] == '9'):
			Board[2][2] = 'X'
		print_board()
		if (check_winner()):
			break
		while(O < 0 or O > 10):
			O = int(input('O, type the number you would like to place an O down in: '))
		if (O == 1 and Board[0][0] == '1'):
			Board[0][0] = 'O'
		elif(O == 2 and Board[0][1] == '2'):
			Board[0][1] = 'O'
		elif(O == 3 and Board[0][2] == '3'):
			Board[0][2] = 'O'
		elif(O == 4 and Board[1][0] == '4'):
			Board[1][0] = 'O'
		elif(O == 5 and Board[1][1] == '5'):
			Board[1][1] = 'O'
		elif(O == 6 and Board[1][2] == '6'):
			Board[1][2] = 'O'
		if (O == 7 and Board[2][0] == '7'):
			Board[2][0] = 'O'
		elif(O == 8 and Board[2][1] == '8'):
			Board[2][1] = 'O'
		elif(O == 9 and Board[2][2] == '9'):
			Board[2][2] = 'O'
		X = 11
		O = 11
	print_board()
	print('Game over')
	
Game()
