# -*- coding: utf-8 -*-
from copy import deepcopy #to fully copy a board state

class GameStatus:


	def __init__(self, board_state, turn_O):

		self.board_state = board_state
		self.turn_O = turn_O
		self.oldScores = 0

		self.winner = ""


	def is_terminal(self):
		"""
        YOUR CODE HERE TO CHECK IF ANY CELL IS EMPTY WITH THE VALUE 0. IF THERE IS NO EMPTY
        THEN YOU SHOULD ALSO RETURN THE WINNER OF THE GAME BY CHECKING THE SCORES FOR EACH PLAYER 
        """
        #Loops through all the rows to check if there is still an open grid cell and if there is then it return no winner and continue.
		for row in self.board_state:
			for cell in row:
				if cell == 0:
					return False, ""
		score = self.get_scores(terminal=True)
  		#If the score is positive than the player won.
		if score > 0:
			return True, "Human"

  		#If the score is negative than the computer won.
		elif score < 0:
			return True, "Computer"
		#If the there are no empty cells and score equals 0 then it's a draw.
		else:
			return True, "Draw"

	def get_scores(self, terminal): #breaks here because is_terminal does not pass any terminal when it calls get_scores()
		"""
        YOUR CODE HERE TO CALCULATE THE SCORES. MAKE SURE YOU ADD THE SCORE FOR EACH PLAYER BY CHECKING 
        EACH TRIPLET IN THE BOARD IN EACH DIRECTION (HORIZONAL, VERTICAL, AND ANY DIAGONAL DIRECTION)
        
        YOU SHOULD THEN RETURN THE CALCULATED SCORE WHICH CAN BE POSITIVE (HUMAN PLAYER WINS),
        NEGATIVE (AI PLAYER WINS), OR 0 (DRAW)
        
        """        
		rows = len(self.board_state)
		cols = len(self.board_state[0])
		scores = 0
		check_point = 3 if terminal else 2
		consecutive = 0
  
        #Checking Rows for triplet
		for i in range(rows):
			#Counter for 3 cells with same value in a row. If cell equals 1 then add 1 to counter,
			#if it equals -1 then subtract 1 from counter.
			consecutive = 0
			for j in range(cols):
				if self.board_state[i][j] == 1:
					consecutive += 1
     				#Adding + 1 to score for human triplet
					if consecutive == check_point:
						consecutive = 0
						scores += 1
				elif self.board_state[i][j] == -1:
					consecutive -= 1
          			#Adding - 1 to score for comupter triplet
					if consecutive == -(check_point):
						consecutive = 0
						scores -= 1
				else:
					consecutive = 0
     
     	#Checking Columns for triplet
		for j in range(cols):
			#Counter for 3 cells with same value in a row. If cell equals 1 then add 1 to counter,
			#if it equals -1 then subtract 1 from counter.
			consecutive = 0
			for i in range(rows):
				if self.board_state[i][j] == 1:
					consecutive += 1
          			#Adding + 1 to score for human triplet
					if consecutive == check_point:
						consecutive = 0
						scores += 1
				elif self.board_state[i][j] == -1:
					consecutive -= 1
          			#Adding - 1 to score for computer triplet
					if consecutive == -(check_point):
						consecutive = 0
						scores -= 1
				else:
					consecutive = 0
     
		#Checking Diagonal 1
		for i in range(rows):
			#Counter for 3 cells with same value in a row. If cell equals 1 then add 1 to counter,
			#if it equals -1 then subtract 1 from counter.
			consecutive = 0
			for j in range(cols):
				if self.board_state[i][j] == 1:
					consecutive += 1
          			#Adding + 1 to score for human triplet
					if consecutive == check_point:
						consecutive = 0
						scores += 1
				elif self.board_state[i][j] == -1:
					consecutive -= 1
          			#Adding - 1 to score for computer triplet
					if consecutive == -(check_point):
						consecutive = 0
						scores -= 1	
				else:
					consecutive = 0
				#Pushes cell to the next row while cols loops normally to go diagonal.
				if i < rows - 1:
					i += 1
    
    	#Checking Diagonal 2
		for i in range(rows):
			#Counter for 3 cells with same value in a row. If cell equals 1 then add 1 to counter,
			#if it equals -1 then subtract 1 from counter.
			consecutive = 0
			for j in range(cols):
				if self.board_state[rows - 1 - i][j] == 1:
					consecutive += 1
          			#Adding + 1 to score for human triplet
					if consecutive == check_point:
						consecutive = 0
						scores += 1
				elif self.board_state[rows - 1 - i][j] == -1:
					consecutive -= 1
          			#Adding - 1 to score for computer triplet
					if consecutive == -(check_point):
						consecutive = 0
						scores -= 1	
				else:
					consecutive = 0
     			#Pushes cell to the next row while cols loops in reverse to go diagonally the other direction.
				if i < rows - 1:
					i += 1
		return scores

	def get_negamax_scores(self, terminal):
		"""
        YOUR CODE HERE TO CALCULATE NEGAMAX SCORES. THIS FUNCTION SHOULD EXACTLY BE THE SAME OF GET_SCORES UNLESS
        YOU SET THE SCORE FOR NEGAMX TO A VALUE THAT IS NOT AN INCREMENT OF 1 (E.G., YOU CAN DO SCORES = SCORES + 100 
                                                                               FOR HUMAN PLAYER INSTEAD OF 
                                                                               SCORES = SCORES + 1)
        """
		rows = len(self.board_state)
		cols = len(self.board_state[0])
		scores = 0
		check_point = 3 if terminal else 2
		consecutive = 0 
  
		#Same code as get_scores function.
  
		#Checking Rows
		for i in range(rows):
			consecutive = 0
			for j in range(cols):
				if self.board_state[i][j] == 1:
					consecutive += 1
					if consecutive == check_point:
						consecutive = 0
						scores += 1
				elif self.board_state[i][j] == -1:
					consecutive -= 1
					if consecutive == -(check_point):
						consecutive = 0
						scores -= 1
				else:
					consecutive = 0
     
     	#Checking Columns
		for j in range(cols):
			consecutive = 0
			for i in range(rows):
				if self.board_state[i][j] == 1:
					consecutive += 1
					if consecutive == check_point:
						consecutive = 0
						scores += 1
				elif self.board_state[i][j] == -1:
					consecutive -= 1
					if consecutive == -(check_point):
						consecutive = 0
						scores -= 1
				else:
					consecutive = 0
     
		#Checking Diagonal 1
		for i in range(rows):
			consecutive = 0
			for j in range(cols):
				if self.board_state[i][j] == 1:
					consecutive += 1
					if consecutive == check_point:
						consecutive = 0
						scores += 1
				elif self.board_state[i][j] == -1:
					consecutive -= 1
					if consecutive == -(check_point):
						consecutive = 0
						scores -= 1	
				else:
					consecutive = 0
				if i < rows - 1:
					i += 1
    
    	#Checking Diagonal 2
		for i in range(rows):
			consecutive = 0
			for j in range(cols):
				if self.board_state[rows - 1 - i][j] == 1:
					consecutive += 1
					if consecutive == check_point:
						consecutive = 0
						scores += 1
				elif self.board_state[rows - 1 - i][j] == -1:
					consecutive -= 1
					if consecutive == -(check_point):
						consecutive = 0
						scores -= 1	
				else:
					consecutive = 0
				if i < rows - 1:
					i += 1
       
		return scores
	    

	def get_moves(self):
		moves = []
		"""
        YOUR CODE HERE TO ADD ALL THE NON EMPTY CELLS TO MOVES VARIABLES AND RETURN IT TO BE USE BY YOUR
        MINIMAX OR NEGAMAX FUNCTIONS
        """
        #Sets rows and cols to the grid size being used.
		rows = len(self.board_state)
		cols = len(self.board_state[0])
  
		#Loops through the grid and pushes the coordinates of any cell that is not empty.
		for i in range(rows):
			for j in range(cols):
				if self.board_state[i][j] == 0:
					moves.append((i, j))
		return moves


	def get_new_state(self, move):
		new_board_state = deepcopy(self.board_state)
		x, y = move[0], move[1]
		new_board_state[x][y] = 1 if self.turn_O else -1
		return GameStatus(new_board_state, not self.turn_O)