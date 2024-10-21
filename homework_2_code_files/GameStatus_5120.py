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
		for row in self.board_state:
			for cell in row:
				if cell == 0:
					return False, ""
				else:
					continue
		_, player_score, ai_score = self.grade_board_state()
		if player_score > ai_score:
			return True, "Human"
		elif player_score < ai_score:
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
	def get_children(self, maximizingPlayer, latest_move):
		children = [] # a list of board states
		children_positions = [] # list of cell positions for child move

		if isinstance(maximizingPlayer, int):
			if maximizingPlayer < 0:
				maximizingPlayer = True
			else:
				maximizingPlayer = False

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

			children, children_positions = self.prioritize_children(children, children_positions, latest_move)
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
			
			children, children_positions = self.prioritize_children(children, children_positions, latest_move)
			return children, children_positions

	def prioritize_children(self, children, children_positions, latest_move):
		board_size = len(self.board_state[0])
		nearest_cells = []


		if latest_move - board_size < 0: #asks if move on left edge
			if latest_move != 0:
				nearest_cells.append(latest_move - 1) #cell ontop
				nearest_cells.append(latest_move + board_size - 1) #cell top left
			if latest_move < board_size - 1:
				nearest_cells.append(latest_move + 1) #cell below
				nearest_cells.append(latest_move + board_size + 1) #cell bottom right
			nearest_cells.append(latest_move + board_size) #cell to the right
		
		elif latest_move + board_size > (board_size ** 2 - 1): #asks if move on right edge
			if latest_move != board_size * (board_size - 1):
				nearest_cells.append(latest_move - 1)
				nearest_cells.append(latest_move - board_size - 1)
			if latest_move < (board_size ** 2 - 1):
				nearest_cells.append(latest_move + 1)
				nearest_cells.append(latest_move - board_size + 1)
			nearest_cells.append(latest_move - board_size) #cell to the left

		elif latest_move % board_size == 0: # asks if move on top edge
			if latest_move != 0:
				nearest_cells.append(latest_move - board_size)
				nearest_cells.append(latest_move - board_size + 1)
			if latest_move != board_size * (board_size - 1):
				nearest_cells.append(latest_move + board_size)
				nearest_cells.append(latest_move + board_size + 1)
			nearest_cells.append(latest_move + 1)

		elif (latest_move + 1) % board_size == 0: #asks if move on bottom edge
			if latest_move != board_size - 1:
				nearest_cells.append(latest_move - board_size)
				nearest_cells.append(latest_move - board_size - 1)
			if latest_move != (board_size ** 2 - 1):
				nearest_cells.append(latest_move + board_size)
				nearest_cells.append(latest_move + board_size - 1)
			nearest_cells.append(latest_move - 1)
		
		else:
			nearest_cells.append(latest_move - 1)
			nearest_cells.append(latest_move + 1)
			nearest_cells.append(latest_move - board_size)
			nearest_cells.append(latest_move + board_size)
			nearest_cells.append(latest_move + board_size - 1)
			nearest_cells.append(latest_move + board_size + 1)
			nearest_cells.append(latest_move - board_size - 1)
			nearest_cells.append(latest_move - board_size + 1)

		for position in nearest_cells:
			for num in range(board_size):
				if position < ((num + 1) * board_size):
					column_pos = num
					break

			if (column_pos, position - (column_pos * board_size)) in children_positions:
				child_index = children_positions.index((column_pos, position - (column_pos * board_size)))

				pop_child_pos = children_positions.pop(child_index)
				children_positions.insert(0, pop_child_pos)

				pop_child = children.pop(child_index)
				children.insert(0, pop_child)

		return children, children_positions




		
				
			



	def grade_board_state(self):
		neg_points = 0
		neg_pairs = 0
		neg_trips = 0
		
		pos_points = 0
		pos_pairs = 0
		pos_trips = 0

		board_length = len(self.board_state)

		#Checking columns
		for index, col in enumerate(self.board_state):
			if index == 0 or index == board_length - 1: #discourage points at left right edges
				consecutive = 0 #reset consecutive at the start of each column
				for cell in col:
					consecutive, _, pos_pairs, pos_trips, _, neg_pairs, neg_trips = self.check_cell_value(
						cell, consecutive,
						pos_points, pos_pairs, pos_trips,
						neg_points, neg_pairs, neg_trips
					)
			else:

				if board_length % 2 == 0: #even board size
					if index < board_length // 2:
						bonus = index + 1
					else:
						bonus = board_length - index
				else: #odd
					if index < board_length // 2:
						bonus = index + 1
					elif index > board_length // 2:
						bonus = board_length - index
					else:
						bonus = board_length

				consecutive = 0 #reset consecutive at the start of each column, encourage points in middle columns
				for cell in col:
					consecutive, pos_points, pos_pairs, pos_trips, neg_points, neg_pairs, neg_trips = self.check_cell_value(
						cell, consecutive,
						pos_points, pos_pairs, pos_trips,
						neg_points, neg_pairs, neg_trips,
						bonus
					)
				

		#Checking rows
		for column_position in range(board_length):
			if column_position == 0 or column_position == board_length - 1: #discourage points at top row and bottom row
				consecutive = 0
				for row_position in range(board_length):
					cell = self.board_state[row_position][column_position]

					consecutive, _, pos_pairs, pos_trips, _, neg_pairs, neg_trips = self.check_cell_value(
						cell, consecutive,
						pos_points, pos_pairs, pos_trips,
						neg_points, neg_pairs, neg_trips
					)
			else:
				if board_length % 2 == 0: #even board size
					if column_position < board_length // 2:
						bonus = column_position + 1
					else:
						bonus = board_length - column_position
				else: #odd
					if column_position < board_length // 2:
						bonus = column_position + 1
					elif column_position > board_length // 2:
						bonus = board_length - column_position
					else:
						bonus = board_length

				consecutive = 0
				for row_position in range(board_length):
					cell = self.board_state[row_position][column_position]
					consecutive, pos_points, pos_pairs, pos_trips, neg_points, neg_pairs, neg_trips = self.check_cell_value(
						cell, consecutive,
						pos_points, pos_pairs, pos_trips,
						neg_points, neg_pairs, neg_trips,
						bonus
					)
					

		#Checking diagonals
		#upper left to lower right
		consecutive = 0
		for ij_index in range(board_length):
			cell = self.board_state[ij_index][ij_index]
			if ij_index != 0 or ij_index != board_length - 1:
				if ij_index < board_length // 2:
					bonus = ij_index + 1
				elif ij_index > board_length // 2:
					bonus = board_length - ij_index
				else:
					bonus = board_length * 2
			consecutive, pos_points, pos_pairs, pos_trips, neg_points, neg_pairs, neg_trips = self.check_cell_value(
				cell, consecutive,
				pos_points, pos_pairs, pos_trips,
				neg_points, neg_pairs, neg_trips,
				bonus
			)

		#lower left to upper right
		consecutive = 0
		for col_index in range(board_length):
			cell_index = (board_length - 1) - col_index
			cell = self.board_state[col_index][cell_index]
			if col_index != 0 or col_index != board_length - 1:
				if col_index < board_length // 2:
					bonus = col_index + 1
				elif col_index > board_length // 2:
					bonus = board_length - col_index
				else:
					bonus = board_length * 2
			consecutive, pos_points, pos_pairs, pos_trips, neg_points, neg_pairs, neg_trips = self.check_cell_value(
				cell, consecutive,
				pos_points, pos_pairs, pos_trips,
				neg_points, neg_pairs, neg_trips,
				bonus
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
		pos_score = pos_points + (4 * board_length * pos_pairs) + (32 * board_length * pos_trips)
		neg_score = -1 * (neg_points + (4 * board_length * neg_pairs) + (32 * board_length * neg_trips))

		board_grade = pos_score + neg_score
		
		return board_grade, pos_trips, neg_trips


	def check_cell_value(self, cell_value, consecutive, pos_points, pos_pairs, pos_trips, neg_points, neg_pairs, neg_trips, bonus = None):
		if cell_value == 1:
			if consecutive < 0:
				consecutive = 0
			consecutive += 1
			if bonus:
				pos_points += bonus
			else:
				pos_points += 1
			if consecutive >= 2:
				pos_pairs += 1
			if consecutive >= 3:
				pos_trips += 1
		elif cell_value == -1:
			if consecutive > 0:
				consecutive = 0
			consecutive -= 1
			if bonus:
				neg_points += bonus
			else:
				neg_points += 1
			if consecutive <= -2:
				neg_pairs += 1
			if consecutive <= -3:
				neg_trips += 1
		else:
			consecutive = 0
		return consecutive, pos_points, pos_pairs, pos_trips, neg_points, neg_pairs, neg_trips
