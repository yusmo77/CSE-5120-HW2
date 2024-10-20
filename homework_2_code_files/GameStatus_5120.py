# -*- coding: utf-8 -*-
from copy import deepcopy #to fully copy a board state
import pdb;

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
		for row in self.board_state:
			for cell in row:
				if cell == 0:
					return False, ""
				else:
					continue
		if self.get_scores() > 0:
			return True, "Human"
		elif self.get_scores() < 0:
			return True, "Computer"
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
		rows = len(self.board_state)
		cols = len(self.board_state[0])
  
		for i in range(rows):
			for j in range(cols):
				if self.board_state[i][j] != 0:
					moves.append(self.board_state[i][j])
      
		return moves


	def get_new_state(self, move):
		new_board_state = self.board_state.copy()
		x, y = move[0], move[1]
		new_board_state[x][y] = 1 if self.turn_O else -1
		return GameStatus(new_board_state, not self.turn_O)

	# Helper function to get children
	def get_children(self, maximizingPlayer):
		children = [] # a list of board states
		children_positions = [] # list of cell positions for child move

		if maximizingPlayer: # will generate children boards with next move as 1
			for col_index in range(len(self.board_state)): #where self.board_state is the cur board state / parent
				for cell_index in range(len(self.board_state[0])):
					if self.board_state[col_index][cell_index] == 0:
						#create board
						child_board = deepcopy(self.board_state)
						child_board[col_index][cell_index] = 1
						#make gamestatus from board
						child_game_status = GameStatus(child_board, not self.turn_O)
						children.append(child_game_status)
						children_positions.append((col_index, cell_index))

			return children, children_positions

		else: # will generate children boards with next move as -1
			for col_index in range(len(self.board_state)): #where self.board_state is the cur board state / parent
				for cell_index in range(len(self.board_state[0])):
					if self.board_state[col_index][cell_index] == 0:
						#create board
						child_board = deepcopy(self.board_state)
						child_board[col_index][cell_index] = -1
						#make gamestatus from board
						child_game_status = GameStatus(child_board, not self.turn_O)
						children.append(child_game_status)
						children_positions.append((col_index, cell_index))

			return children, children_positions

	def grade_board_state(self):
		pdb.set_trace()
		neg_points = 0
		neg_pairs = 0
		neg_trips = 0
		
		pos_points = 0
		pos_pairs = 0
		pos_trips = 0

		board_length = len(self.board_state)

		#Checking columns
		for col in self.board_state:
			consecutive = 0 #reset consecutive at the start of each column
			for cell in col:
				consecutive, pos_points, pos_pairs, pos_trips, neg_points, neg_pairs, neg_trips = self.check_cell_value(
					cell, consecutive,
					pos_points, pos_pairs, pos_trips,
					neg_points, neg_pairs, neg_trips
				)
				

		#Checking rows
		for column_position in range(board_length):
			consecutive = 0
			for row_position in range(board_length):
				cell = self.board_state[row_position][column_position]

				consecutive, pos_points, pos_pairs, pos_trips, neg_points, neg_pairs, neg_trips = self.check_cell_value(
					cell, consecutive,
					pos_points, pos_pairs, pos_trips,
					neg_points, neg_pairs, neg_trips
				)

		#Checking diagonals
		#upper left to lower right
		consecutive = 0
		for ij_index in range(board_length):
			cell = self.board_state[ij_index][ij_index]
			consecutive, pos_points, pos_pairs, pos_trips, neg_points, neg_pairs, neg_trips = self.check_cell_value(
				cell, consecutive,
				pos_points, pos_pairs, pos_trips,
				neg_points, neg_pairs, neg_trips
			)

		#lower left to upper right
		consecutive = 0
		for col_index in range(board_length):
			cell_index = (board_length - 1) - col_index
			cell = self.board_state[col_index][cell_index]

			consecutive, pos_points, pos_pairs, pos_trips, neg_points, neg_pairs, neg_trips = self.check_cell_value(
				cell, consecutive,
				pos_points, pos_pairs, pos_trips,
				neg_points, neg_pairs, neg_trips
			)
		
		#additional diagonals
		if len(self.board_state) > 3:
			additional_diagonals = len(self.board_state) - 3

			for diagonal_num in range(additional_diagonals):
				diagonal_length = diagonal_num + 3

				#above main diagonal going from lower left to upper right
				consecutive = 0
				for col_position in range(diagonal_length):
					cell_position = (diagonal_length - 1) - col_position
					cell = self.board_state[col_position][cell_position]
					
					consecutive, pos_points, pos_pairs, pos_trips, neg_points, neg_pairs, neg_trips = self.check_cell_value(
						cell, consecutive,
						pos_points, pos_pairs, pos_trips,
						neg_points, neg_pairs, neg_trips
					)

				#below main diagonal going from lower left to upper right
				consecutive = 0
				for length in range(diagonal_length):
					col_position = (additional_diagonals - diagonal_num) + length
					cell_position = (len(self.board_state[0]) - 1) - length
					cell = self.board_state[col_position][cell_position]

					consecutive, pos_points, pos_pairs, pos_trips, neg_points, neg_pairs, neg_trips = self.check_cell_value(
						cell, consecutive,
						pos_points, pos_pairs, pos_trips,
						neg_points, neg_pairs, neg_trips
					)

				#above main diagonal going from upper left to lower right
				consecutive = 0
				for length in range(diagonal_length):
					col_position = (additional_diagonals - diagonal_num) + length
					cell_position = length
					cell = self.board_state[col_position][cell_position]

					consecutive, pos_points, pos_pairs, pos_trips, neg_points, neg_pairs, neg_trips = self.check_cell_value(
						cell, consecutive,
						pos_points, pos_pairs, pos_trips,
						neg_points, neg_pairs, neg_trips
					)
				
				#below main diagonal going from upper left to lower right
				consecutive = 0
				for length in range(diagonal_length):
					col_position = length
					cell_position = (additional_diagonals - diagonal_num) + length
					cell = self.board_state[col_position][cell_position]

					consecutive, pos_points, pos_pairs, pos_trips, neg_points, neg_pairs, neg_trips = self.check_cell_value(
						cell, consecutive,
						pos_points, pos_pairs, pos_trips,
						neg_points, neg_pairs, neg_trips
					)
			
		#calculating score
		pos_score = pos_points + (2 * pos_pairs) + (20 * pos_trips)
		neg_score = -1 * (neg_points + (2 * neg_pairs) + (20 * neg_trips))

		board_grade = pos_score + neg_score
		
		return pos_trips, neg_trips, board_grade


	def check_cell_value(self, cell_value, consecutive, pos_points, pos_pairs, pos_trips, neg_points, neg_pairs, neg_trips):
		if cell_value == 1:
			if consecutive < 0:
				consecutive = 0
			consecutive += 1
			pos_points += 1
			if consecutive >= 2:
				pos_pairs += 1
			if consecutive >= 3:
				pos_trips += 1
		elif cell_value == -1:
			if consecutive > 0:
				consecutive = 0
			consecutive -= 1
			neg_points += 1
			if consecutive <= -2:
				neg_pairs += 1
			if consecutive <= -3:
				neg_trips += 1
		else:
			consecutive = 0
		return consecutive, pos_points, pos_pairs, pos_trips, neg_points, neg_pairs, neg_trips
