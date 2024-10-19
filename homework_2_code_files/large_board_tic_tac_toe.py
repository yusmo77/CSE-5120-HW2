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

mode = "player_vs_ai" # default mode for playing the game (player vs AI)

class RandomBoardTicTacToe:
    def __init__(self, size = (600, 600)):

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
        self. OFFSET = 5

        self.CIRCLE_COLOR = (140, 146, 172)
        self.CROSS_COLOR = (140, 146, 172)

        # This sets the WIDTH and HEIGHT of each grid location
        self.WIDTH = self.size[0]/self.GRID_SIZE - self.OFFSET
        self.HEIGHT = (self.size[1] - 145)/self.GRID_SIZE - self.OFFSET

        # This sets the margin between each cell
        self.MARGIN = 5

        # Initialize pygame
        pygame.init()
        self.game_reset()

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
                col = j * self.MARGIN + j * self.HEIGHT + 145
                pygame.draw.rect(self.screen, self.WHITE, (row, col, self.WIDTH, self.HEIGHT))
        pygame.draw.rect(self.screen, self.WHITE, (0, 0, 600, 140))
        
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
        pygame.draw.rect(self.screen, self.BLACK, (70, 25, 80, 30))
        button_rect = pygame.draw.rect(self.screen, self.GREEN_BLUE, (72, 27, 75, 25))
        start_rect.center = (button_rect.x + button_rect.width // 2, button_rect.y + button_rect.height // 2)
        self.screen.blit(start_text, start_rect)
        
        #4x4 Board
        font = pygame.font.SysFont('Arial', 18)
        start_text = font.render('4x4' , True , self.WHITE)
        start_rect = start_text.get_rect()
        pygame.draw.rect(self.screen, self.BLACK, (70, 65, 80, 30))
        button_rect = pygame.draw.rect(self.screen, self.GREEN_BLUE, (72, 67, 75, 25))
        start_rect.center = (button_rect.x + button_rect.width // 2, button_rect.y + button_rect.height // 2)
        self.screen.blit(start_text, start_rect)
        
        #5x5 Board
        font = pygame.font.SysFont('Arial', 18)
        start_text = font.render('5x5' , True , self.WHITE)
        start_rect = start_text.get_rect()
        pygame.draw.rect(self.screen, self.BLACK, (70, 105, 80, 30))
        button_rect = pygame.draw.rect(self.screen, self.GREEN_BLUE, (72, 107, 75, 25))
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
        pygame.draw.rect(self.screen, self.BLACK, (445, 25, 85, 30))
        button_rect = pygame.draw.rect(self.screen, self.GREEN_BLUE, (447, 27, 80, 25))
        start_rect.center = (button_rect.x + button_rect.width // 2, button_rect.y + button_rect.height // 2)
        self.screen.blit(start_text, start_rect)
        
        #Minimax game
        font = pygame.font.SysFont('Arial', 18)
        start_text = font.render('Minimax' , True , self.WHITE)
        start_rect = start_text.get_rect()
        pygame.draw.rect(self.screen, self.BLACK, (445, 65, 85, 30))
        button_rect = pygame.draw.rect(self.screen, self.GREEN_BLUE, (447, 67, 80, 25))
        start_rect.center = (button_rect.x + button_rect.width // 2, button_rect.y + button_rect.height // 2)
        self.screen.blit(start_text, start_rect)
        
        #Winner
        font = pygame.font.SysFont('Arial', 18)
        start_text = font.render('Winner: ', 1 , self.BLACK)
        #winner = font.render(str(self.winner), 1, self.BLACK)
        self.screen.blit(start_text, (200, 80))
        #self.screen.blit(winner, (220, 80))
        
        #Scores
        font = pygame.font.SysFont('Arial', 18)
        start_text = font.render('Scores (Human: ##, Computer: ## ) ' , True , self.BLACK)
        self.screen.blit(start_text, (200, 120))
        
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
        radius = min(self.WIDTH, self.HEIGHT) // 3
        circle_x = x * (self.WIDTH + self.MARGIN)
        circle_y = y * (self.HEIGHT + self.MARGIN)
        pygame.draw.circle(self.screen, self.CIRCLE_COLOR, (circle_x, circle_y), radius)
        pygame.display.update()

    def draw_cross(self, x, y):
        """
        YOUR CODE HERE TO DRAW THE CROSS FOR THE CROSS PLAYER AT THE CELL THAT IS SELECTED VIA THE gui
        """
        radius = self.WIDTH // 2
        cross_x = x * (self.WIDTH + self.MARGIN)
        cross_y = y * (self.HEIGHT + self.MARGIN)
        pygame.draw.line(self.screen, self.CROSS_COLOR,(cross_x, cross_y), (cross_x + self.width, cross_y + self.height), radius)
        pygame.draw.line(self.screen, self.CROSS_COLOR,(cross_y, cross_x), (cross_y + self.height, cross_x + self.width), radius)

    def is_game_over(self):

        """
        YOUR CODE HERE TO SEE IF THE GAME HAS TERMINATED AFTER MAKING A MOVE. YOU SHOULD USE THE IS_TERMINAL()
        FUNCTION FROM GAMESTATUS_5120.PY FILE (YOU WILL FIRST NEED TO COMPLETE IS_TERMINAL() FUNCTION)
        
        YOUR RETURN VALUE SHOULD BE TRUE OR FALSE TO BE USED IN OTHER PARTS OF THE GAME
        """
        return self.game_state.is_terminal
    

    def move(self, move):
        self.game_state = self.game_state.get_new_state(move)


    def play_ai(self):
        """
        YOUR CODE HERE TO CALL MINIMAX OR NEGAMAX DEPENDEING ON WHICH ALGORITHM SELECTED FROM THE GUI
        ONCE THE ALGORITHM RETURNS THE BEST MOVE TO BE SELECTED, YOU SHOULD DRAW THE NOUGHT (OR CIRCLE DEPENDING
        ON WHICH SYMBOL YOU SELECTED FOR THE AI PLAYER)
        
        THE RETURN VALUES FROM YOUR MINIMAX/NEGAMAX ALGORITHM SHOULD BE THE SCORE, MOVE WHERE SCORE IS AN INTEGER
        NUMBER AND MOVE IS AN X,Y LOCATION RETURNED BY THE AGENT
        """
        
        
        self.change_turn()
        pygame.display.update()
        terminal = self.game_state.is_terminal()
        """ USE self.game_state.get_scores(terminal) HERE TO COMPUTE AND DISPLAY THE FINAL SCORES """
        if(terminal):
            return self.game_state.get_scores(terminal)



    def game_reset(self):
        rows = self.GRID_SIZE
        cols = self.GRID_SIZE
  
        reset_game = [[0 for i in range(rows)] for j in range(cols)]
        self.game_state = GameStatus(reset_game, True)
        self.draw_game()
        """
        YOUR CODE HERE TO RESET THE BOARD TO VALUE 0 FOR ALL CELLS AND CREATE A NEW GAME STATE WITH NEWLY INITIALIZED
        BOARD STATE
        """
        
        pygame.display.update()

    def play_game(self, mode = "player_vs_ai"):
        done = False

        clock = pygame.time.Clock()


        while not done:
            for event in pygame.event.get():  # User did something
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

tictactoegame = RandomBoardTicTacToe()
tictactoegame.play_game()
"""
YOUR CODE HERE TO SELECT THE OPTIONS VIA THE GUI CALLED FROM THE ABOVE LINE
AFTER THE ABOVE LINE, THE USER SHOULD SELECT THE OPTIONS AND START THE GAME. 
YOUR FUNCTION PLAY_GAME SHOULD THEN BE CALLED WITH THE RIGHT OPTIONS AS SOON
AS THE USER STARTS THE GAME
"""
