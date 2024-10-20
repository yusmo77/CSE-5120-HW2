"""
PLEASE READ THE COMMENTS BELOW AND THE HOMEWORK DESCRIPTION VERY CAREFULLY BEFORE YOU START CODING

 The file where you will need to create the GUI which should include (i) drawing the grid, (ii) call your Minimax/Negamax functions
 at each step of the game, (iii) allowing the controls on the GUI to be managed (e.g., setting board size, using 
                                                                                 Minimax or Negamax, and other options)
 In the example below, grid creation is supported using pygame which you can use. You are free to use any other 
 library to create better looking GUI with more control. In the __init__ function, GRID_SIZE (Line number 36) is the variable that
 sets the size of the grid. Once you have the Minimax code written in multiAgents.py file, it is recommended to test
 your algorithm (with alpha-beta pruning) on a 3x3 GRID_SIZE to see if the computer always tries for a draw and does 
 not let you win the game. Here is a video tutorial for using pygame to create grids http://youtu.be/mdTeqiWyFnc
 
 
 PLEASE CAREFULLY SEE THE PORTIONS OF THE CODE/FUNCTIONS WHERE IT INDICATES "YOUR CODE BELOW" TO COMPLETE THE SECTIONS
 
"""
import pygame
import numpy as np
from GameStatus_5120 import GameStatus
from multiAgents import minimax, negamax
import sys, random

#Helper imports
from math import sqrt
import pdb; pdb.set_trace()

mode = "player_vs_ai" # default mode for playing the game (player vs AI)

class RandomBoardTicTacToe:
    def __init__(self, size = (600, 600)):

        #game data variables
        self.cell_boundaries = []
        self.cell_centers = None
        self.board_state = None
        self.game_state = None

        self.size = self.width, self.height = size
        # Define some colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.BLUE = (100, 149, 237)
        self.GREEN_BLUE = (8, 143, 143)

        # Grid Size
        self.GRID_SIZE = 3
        self.OFFSET = 5

        self.CIRCLE_COLOR = (140, 146, 172)
        self.CROSS_COLOR = (140, 146, 172)

        # This sets the margin between each cell
        self.MARGIN = 5

        ## VIEWPORT MARGINS
        self.VIEWPORT_TOPMARGIN = self.height * 0.20
        self.VIEWPORT_SIDEMARGINS = self.height * 0.10

        #cell WIDTH and HEIGHT be calculated based on the GRID_SIZE
        self.HEIGHT, self.WIDTH = self.define_cell_size()

        # Initialize pygame
        pygame.init()
        self.game_reset(self.GRID_SIZE) #this overrides parameter default with class default

    def draw_game(self):
        # Create a 2 dimensional array using the column and row variables
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Tic Tac Toe Random Grid")
        self.screen.fill(self.BLACK)
        
        """
        YOUR CODE HERE TO DRAW THE GRID OTHER CONTROLS AS PART OF THE GUI
        """
        # Draw the grid
        for i in range(0, self.GRID_SIZE):
            for j in range(0, self.GRID_SIZE):
                row = i * self.MARGIN + i * self.WIDTH
                col = j * self.MARGIN + j * self.HEIGHT
                pygame.draw.rect(self.screen, self.WHITE, (row + 65, col + 125, self.WIDTH, self.HEIGHT)) #first two params are row/col + side/top margin + offset
                self.cell_boundaries.append((row + 65, col + 125, row + 65 + self.WIDTH, col + 125 + self.HEIGHT))
        self.cell_centers = self.get_board_centers()
        pygame.draw.rect(self.screen, self.WHITE, (0, 0, 600, 120))
        pygame.draw.rect(self.screen, self.WHITE, (0, 0, 60, 600))
        pygame.draw.rect(self.screen, self.WHITE, (540, 0, 60, 600))
        
        #Start Button
        font = pygame.font.SysFont('Arial', 18)
        start_text = font.render('Start' , True , self.WHITE)
        start_rect = start_text.get_rect()
        pygame.draw.rect(self.screen, self.BLACK, (256, 5, 80, 30))
        button_rect = pygame.draw.rect(self.screen, self.GREEN_BLUE, (258, 7, 75, 25))
        start_rect.center = (button_rect.x + button_rect.width // 2, button_rect.y + button_rect.height // 2)
        self.screen.blit(start_text, start_rect)
        
        #Board text
        font = pygame.font.SysFont('Arial', 18)
        start_text = font.render('Board Size' , True , self.BLACK)
        self.screen.blit(start_text, (65, 5))
        
        #3x3 Board
        font = pygame.font.SysFont('Arial', 18)
        start_text = font.render('3x3' , True , self.WHITE)
        start_rect = start_text.get_rect()
        pygame.draw.rect(self.screen, self.BLACK, (65, 25, 80, 30))
        button_rect = pygame.draw.rect(self.screen, self.GREEN_BLUE, (67, 27, 75, 25))
        start_rect.center = (button_rect.x + button_rect.width // 2, button_rect.y + button_rect.height // 2)
        self.screen.blit(start_text, start_rect)
        
        #4x4 Board
        font = pygame.font.SysFont('Arial', 18)
        start_text = font.render('4x4' , True , self.WHITE)
        start_rect = start_text.get_rect()
        pygame.draw.rect(self.screen, self.BLACK, (65, 57, 80, 30))
        button_rect = pygame.draw.rect(self.screen, self.GREEN_BLUE, (67, 59, 75, 25))
        start_rect.center = (button_rect.x + button_rect.width // 2, button_rect.y + button_rect.height // 2)
        self.screen.blit(start_text, start_rect)
        
        #5x5 Board
        font = pygame.font.SysFont('Arial', 18)
        start_text = font.render('5x5' , True , self.WHITE)
        start_rect = start_text.get_rect()
        pygame.draw.rect(self.screen, self.BLACK, (65, 89, 80, 30))
        button_rect = pygame.draw.rect(self.screen, self.GREEN_BLUE, (67, 91, 75, 25))
        start_rect.center = (button_rect.x + button_rect.width // 2, button_rect.y + button_rect.height // 2)
        self.screen.blit(start_text, start_rect)
        
        #Gamemode
        font = pygame.font.SysFont('Arial', 18)
        start_text = font.render('Gamemode' , True , self.BLACK)
        self.screen.blit(start_text, (440, 5))
        
        #Negamax game
        font = pygame.font.SysFont('Arial', 18)
        start_text = font.render('Negamax' , True , self.WHITE)
        start_rect = start_text.get_rect()
        pygame.draw.rect(self.screen, self.BLACK, (440, 25, 85, 30))
        button_rect = pygame.draw.rect(self.screen, self.GREEN_BLUE, (442, 27, 80, 25))
        start_rect.center = (button_rect.x + button_rect.width // 2, button_rect.y + button_rect.height // 2)
        self.screen.blit(start_text, start_rect)

        #Minimax game
        font = pygame.font.SysFont('Arial', 18)
        start_text = font.render('Minimax' , True , self.WHITE)
        start_rect = start_text.get_rect()
        pygame.draw.rect(self.screen, self.BLACK, (440, 57, 85, 30))
        button_rect = pygame.draw.rect(self.screen, self.GREEN_BLUE, (442, 60, 80, 25))
        start_rect.center = (button_rect.x + button_rect.width // 2, button_rect.y + button_rect.height // 2)
        self.screen.blit(start_text, start_rect)
        
        #Winner
        font = pygame.font.SysFont('Arial', 18)
        start_text = font.render('Winner: ', 1 , self.BLACK)
        self.screen.blit(start_text, (200, 50))
        
        #Scores
        font = pygame.font.SysFont('Arial', 18)
        start_text = font.render('Scores (Human: ##, Computer: ## ) ' , True , self.BLACK)
        self.screen.blit(start_text, (200, 80))
        
        pygame.display.update()

    def change_turn(self):

        if(self.game_state.turn_O):
            pygame.display.set_caption("Tic Tac Toe - O's turn")
        else:
            pygame.display.set_caption("Tic Tac Toe - X's turn")


    def draw_circle(self, x, y):
        """
        YOUR CODE HERE TO DRAW THE CIRCLE FOR THE NOUGHTS PLAYER
        """
        outer_width = int(self.WIDTH * 0.40)
        inner_width = int(self.WIDTH * 0.25)
        pygame.draw.circle(self.screen, self.BLUE, (x, y), outer_width)
        pygame.draw.circle(self.screen, self.WHITE, (x, y), inner_width)
        pygame.display.update()

    def draw_cross(self, x, y):
        """
        YOUR CODE HERE TO DRAW THE CROSS FOR THE CROSS PLAYER AT THE CELL THAT IS SELECTED VIA THE gui
        """
        #twoards corner positions
        right_x = x - (self.WIDTH // 3)
        left_x = x + (self.WIDTH // 3)
        top_y = y - (self.HEIGHT // 3)
        bottom_y = y + (self.HEIGHT // 3)

        line_width = int(self.WIDTH * 0.20)
        pygame.draw.line(self.screen, self.RED, (right_x, top_y), (left_x, bottom_y), line_width)
        pygame.draw.line(self.screen, self.RED, (right_x, bottom_y), (left_x, top_y), line_width)

    def is_game_over(self):

        """
        YOUR CODE HERE TO SEE IF THE GAME HAS TERMINATED AFTER MAKING A MOVE. YOU SHOULD USE THE IS_TERMINAL()
        FUNCTION FROM GAMESTATUS_5120.PY FILE (YOU WILL FIRST NEED TO COMPLETE IS_TERMINAL() FUNCTION)
        
        YOUR RETURN VALUE SHOULD BE TRUE OR FALSE TO BE USED IN OTHER PARTS OF THE GAME
        """
        return self.game_state.is_terminal
    

    def move(self, move):
        self.game_state = self.game_state.get_new_state(move)


    def play_ai(self, mode = "minimax"):
        """
        YOUR CODE HERE TO CALL MINIMAX OR NEGAMAX DEPENDEING ON WHICH ALGORITHM SELECTED FROM THE GUI
        ONCE THE ALGORITHM RETURNS THE BEST MOVE TO BE SELECTED, YOU SHOULD DRAW THE NOUGHT (OR CIRCLE DEPENDING
        ON WHICH SYMBOL YOU SELECTED FOR THE AI PLAYER)
        
        THE RETURN VALUES FROM YOUR MINIMAX/NEGAMAX ALGORITHM SHOULD BE THE SCORE, MOVE WHERE SCORE IS AN INTEGER
        NUMBER AND MOVE IS AN X,Y LOCATION RETURNED BY THE AGENT
        """
        
        
        self.change_turn()
        pygame.display.update()

        if mode == "minimax":
            value, best_move = minimax(self.game_state, 3, False) #depth hardcoded to 3 for testing

        terminal = self.game_state.is_terminal()
        """ USE self.game_state.get_scores(terminal) HERE TO COMPUTE AND DISPLAY THE FINAL SCORES """
        if(terminal[0]):
            return self.game_state.get_scores(terminal)
        
        return best_move

    #for testing purposes default grid_size is 3
    def game_reset(self, grid_size = 3):
        self.GRID_SIZE = grid_size
        self.board_state = []
        
        for i in range (self.GRID_SIZE):
            self.board_state.append([0] * self.GRID_SIZE)

        self.game_state = GameStatus(self.board_state, True)

        self.draw_game()
        """
        YOUR CODE HERE TO RESET THE BOARD TO VALUE 0 FOR ALL CELLS AND CREATE A NEW GAME STATE WITH NEWLY INITIALIZED
        BOARD STATE
        """
        
        pygame.display.update()

    #currently only handles cell click events
    def play_game(self, mode = "player_vs_ai"):
        done = False

        clock = pygame.time.Clock()

        #keeping track of column start and ends to find cell to change later
        column_ends = []
        for num in range(self.GRID_SIZE):
            low = (num * self.GRID_SIZE) 
            high = (num + 1) * self.GRID_SIZE - 1
            column_ends.append((low, high))

        while not done:
            for event in pygame.event.get():  # User did something

                #get mouse click position (x, y)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    cell_selected = self.check_mouse_selection(mouse_pos[0], mouse_pos[1])

                    if isinstance(cell_selected, int):
                        #PLAYER ACTIONS
                        #UPDATE GAMESTATE; for each column check if selected cell is within that range
                        for index, column_range in enumerate(column_ends): 
                            if cell_selected >= column_range[0] and cell_selected <= column_range[1]:
                                self.game_state = self.game_state.get_new_state((index, cell_selected - column_range[0]))
                                break 

                        self.draw_circle(self.cell_centers[cell_selected][0], self.cell_centers[cell_selected][1])

                        #AI ACTIONS
                        ai_move = self.play_ai() #move given in col,cell format convert to cell number {1, 2, to nxn}
                        ai_cell_selected = ai_move[0] * self.GRID_SIZE + ai_move[1]
                        #UPDATE GAMESTATE
                        for index, column_range in enumerate(column_ends): 
                            if ai_cell_selected >= column_range[0] and ai_cell_selected <= column_range[1]:
                                self.game_state = self.game_state.get_new_state((index, ai_cell_selected - column_range[0]))
                                break 

                        self.draw_cross(self.cell_centers[ai_cell_selected][0], self.cell_centers[ai_cell_selected][1])
                        print('AI Move:', ai_move)
                    else:
                        pass
                """
                YOUR CODE HERE TO CHECK IF THE USER CLICKED ON A GRID ITEM. EXIT THE GAME IF THE USER CLICKED EXIT
                """
                
                """
                YOUR CODE HERE TO HANDLE THE SITUATION IF THE GAME IS OVER. IF THE GAME IS OVER THEN DISPLAY THE SCORE,
                THE WINNER, AND POSSIBLY WAIT FOR THE USER TO CLEAR THE BOARD AND START THE GAME AGAIN (OR CLICK EXIT)
                """
                    
                """
                YOUR CODE HERE TO NOW CHECK WHAT TO DO IF THE GAME IS NOT OVER AND THE USER SELECTED A NON EMPTY CELL
                IF CLICKED A NON EMPTY CELL, THEN GET THE X,Y POSITION, SET ITS VALUE TO 1 (SELECTED BY HUMAN PLAYER),
                DRAW CROSS (OR NOUGHT DEPENDING ON WHICH SYMBOL YOU CHOSE FOR YOURSELF FROM THE gui) AND CALL YOUR 
                PLAY_AI FUNCTION TO LET THE AGENT PLAY AGAINST YOU
                """
                
                # if event.type == pygame.MOUSEBUTTONUP:
                    # Get the position
                    
                    # Change the x/y screen coordinates to grid coordinates
                    
                    # Check if the game is human vs human or human vs AI player from the GUI. 
                    # If it is human vs human then your opponent should have the value of the selected cell set to -1
                    # Then draw the symbol for your opponent in the selected cell
                    # Within this code portion, continue checking if the game has ended by using is_terminal function
                    
            # Update the screen with what was drawn.
            pygame.display.update()

        pygame.quit()

    #HELPER FUNCTIONS
    '''
    args:
        x, y; mouse click coordinates

    returns:
        INTS:
            best_index; index of cell that is closest to click
        STRINGS:
            '3x3', '4x4', '5x5'; board size options
            'negamax', 'minimax'; game mode options
            'start'; start button
            'no_option'; no cell or option selected
    '''
    def check_mouse_selection(self, x, y):

        #around options
        if y < self.VIEWPORT_TOPMARGIN:
            #check if clicked on board opts
            if x > 67 and x < 142:
                if y > 27 and y < 52:
                    return '3x3'
                if y > 59 and y < 84:
                    return '4x4'
                if y > 91 and y < 116:
                    return '5x5'
                else:
                    return 'no_option'
            #check if clicked on game opts
            elif x > 442 and x < 552:
                if y > 27 and y < 52:
                    return 'negamax'
                if y > 60 and y < 85:
                    return 'minimax'
                else:
                    return 'no_option'
            #check if clicked on start
            elif y > 7 and y < 32 and x > 258 and x < 333:
                return 'start'
            else:
                return 'no_option'

        #around play board
        elif y > self.VIEWPORT_TOPMARGIN and x > self.VIEWPORT_SIDEMARGINS and x < self.width - self.VIEWPORT_SIDEMARGINS:
            #unforntuatly checks all cells for now
            best_distance = float('inf')
            for index, center in enumerate(self.cell_centers):
                if best_distance > sqrt((x - center[0])**2 + (y - center[1])**2):
                    best_distance = sqrt((x - center[0])**2 + (y - center[1])**2)
                    best_index = index
            return best_index
        else:
            return 'no_option'

    def get_board_centers(self):
        centers = []

        for cell in self.cell_boundaries:
            x = (cell[0] + cell[2]) // 2
            y = (cell[1] + cell[3]) // 2
            centers.append((x, y))
        
        return centers
    

    def define_cell_size(self):
        ## we have n+1 grid lines to render play board
        grid_line_budget = self.OFFSET * (self.GRID_SIZE + 1)

        ## max height and width for the grid including grid lines and cells
        max_grid_height = self.height - self.VIEWPORT_TOPMARGIN - grid_line_budget
        max_grid_width = self.width - (self.VIEWPORT_SIDEMARGINS * 2) - grid_line_budget

        ## cell length
        cell_height = max_grid_height // self.GRID_SIZE
        cell_width = max_grid_width // self.GRID_SIZE

        return cell_height, cell_width

tictactoegame = RandomBoardTicTacToe()
tictactoegame.play_game()
"""
YOUR CODE HERE TO SELECT THE OPTIONS VIA THE GUI CALLED FROM THE ABOVE LINE
AFTER THE ABOVE LINE, THE USER SHOULD SELECT THE OPTIONS AND START THE GAME. 
YOUR FUNCTION PLAY_GAME SHOULD THEN BE CALLED WITH THE RIGHT OPTIONS AS SOON
AS THE USER STARTS THE GAME
"""
