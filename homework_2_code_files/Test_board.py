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
from Test_GameStatus import GameStatus
from Test_Agents import minimax, negamax
import sys, random

mode = "player_vs_ai" # default mode for playing the game (player vs AI)

class RandomBoardTicTacToe:
    def __init__(self, size = (600, 600)):
        
        self.search = "negamax"
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
        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):
                row = i * self.MARGIN + i * self.WIDTH
                col = j * self.MARGIN + j * self.HEIGHT + 145
                pygame.draw.rect(self.screen, self.WHITE, (row, col, self.WIDTH, self.HEIGHT))
        #White rectangle background for the ui buttons.
        pygame.draw.rect(self.screen, self.WHITE, (0, 0, 600, 140))
        
        #Draws the Start Button and centers it
        font = pygame.font.SysFont('Arial', 18)
        start_text = font.render('Start' , True , self.WHITE)
        start_rect = start_text.get_rect()
        pygame.draw.rect(self.screen, self.BLACK, (256, 5, 80, 30))
        self.start_button_rect = pygame.draw.rect(self.screen, self.GREEN_BLUE, (258, 7, 75, 25))
        start_rect.center = (self.start_button_rect.x + self.start_button_rect.width // 2, self.start_button_rect.y + self.start_button_rect.height // 2)
        self.screen.blit(start_text, start_rect)
        
        #Board size text
        start_text = font.render('Board Size' , True , self.BLACK)
        self.screen.blit(start_text, (65, 5))
        
        #Draws the 3x3 board Button and centers it.
        threeb_text = font.render('3x3' , True , self.WHITE)
        threeb_rect = threeb_text.get_rect()
        pygame.draw.rect(self.screen, self.BLACK, (70, 25, 80, 30))
        self.three_button_rect = pygame.draw.rect(self.screen, self.GREEN_BLUE, (72, 27, 75, 25))
        threeb_rect.center = (self.three_button_rect.x + self.three_button_rect.width // 2, self.three_button_rect.y + self.three_button_rect.height // 2)
        self.screen.blit(threeb_text, threeb_rect)
        
        #Draws the 4x4 board Button and centers it.
        fourb_text = font.render('4x4' , True , self.WHITE)
        fourb_rect = fourb_text.get_rect()
        pygame.draw.rect(self.screen, self.BLACK, (70, 65, 80, 30))
        self.four_button_rect = pygame.draw.rect(self.screen, self.GREEN_BLUE, (72, 67, 75, 25))
        fourb_rect.center = (self.four_button_rect.x + self.four_button_rect.width // 2, self.four_button_rect.y + self.four_button_rect.height // 2)
        self.screen.blit(fourb_text, fourb_rect)
        
        #Draws the 5x5 board Button and centers it.
        fiveb_text = font.render('5x5' , True , self.WHITE)
        fiveb_rect = fiveb_text.get_rect()
        pygame.draw.rect(self.screen, self.BLACK, (70, 105, 80, 30))
        self.five_button_rect = pygame.draw.rect(self.screen, self.GREEN_BLUE, (72, 107, 75, 25))
        fiveb_rect.center = (self.five_button_rect.x + self.five_button_rect.width // 2, self.five_button_rect.y + self.five_button_rect.height // 2)
        self.screen.blit(fiveb_text, fiveb_rect)
        
        #Gamemode text
        gamemode_text = font.render('Gamemode' , True , self.BLACK)
        self.screen.blit(gamemode_text, (440, 5))
        
        #Draws the negamax search algorithm Button and centers it.
        negmax_text = font.render('Negamax' , True , self.WHITE)
        negmax_rect = negmax_text.get_rect()
        pygame.draw.rect(self.screen, self.BLACK, (445, 25, 85, 30))
        self.neg_button_rect = pygame.draw.rect(self.screen, self.GREEN_BLUE, (447, 27, 80, 25))
        negmax_rect.center = (self.neg_button_rect.x + self.neg_button_rect.width // 2, self.neg_button_rect.y + self.neg_button_rect.height // 2)
        self.screen.blit(negmax_text, negmax_rect)
        
        #Draws the minimax search algorithm Button and centers it.
        minimax_text = font.render('Minimax' , True , self.WHITE)
        minimax_rect = minimax_text.get_rect()
        pygame.draw.rect(self.screen, self.BLACK, (445, 65, 85, 30))
        self.mini_button_rect = pygame.draw.rect(self.screen, self.GREEN_BLUE, (447, 67, 80, 25))
        minimax_rect.center = (self.mini_button_rect.x + self.mini_button_rect.width // 2, self.mini_button_rect.y + self.mini_button_rect.height // 2)
        self.screen.blit(minimax_text, minimax_rect)
        
        #Winner text
        pygame.draw.rect(self.screen, self.WHITE, (200, 80, 200, 30))
        winner_text = font.render('Winner: ', 1 , self.BLACK)
        self.screen.blit(winner_text, (200, 80))
        
        #Scores text
        pygame.draw.rect(self.screen, self.WHITE, (200, 120, 200, 20))
        score_text = font.render('Scores: ' , True , self.BLACK)
        self.screen.blit(score_text, (200, 120))
        
        pygame.display.update()

    #When called will change the turn from player to computer or player to player to place their piece.
    def change_turn(self):

        if(self.game_state.turn_O):
            pygame.display.set_caption("Tic Tac Toe - O's turn")
        else:
            pygame.display.set_caption("Tic Tac Toe - X's turn")


    def draw_circle(self, x, y):
        """
        YOUR CODE HERE TO DRAW THE CIRCLE FOR THE NOUGHTS PLAYER
        """
        #Makes the width/radius for both the circles being used.
        outer_width = int(self.WIDTH * 0.40)
        inner_width = int(self.WIDTH * 0.25)
        
        #Fits the circle inside the grid cell depending on the grid size.
        circle_x = x * (self.WIDTH + self.MARGIN) + self.WIDTH // 2
        circle_y = y * (self.HEIGHT + self.MARGIN) + self.HEIGHT // 2 + 145
        
        #Draws the tic tac toe circle with two circles one smaller on top the bigger one.
        pygame.draw.circle(self.screen, self.BLUE, (circle_x, circle_y), outer_width)
        pygame.draw.circle(self.screen, self.WHITE, (circle_x, circle_y), inner_width)
        pygame.display.update()

    def draw_cross(self, x, y):
        """
        YOUR CODE HERE TO DRAW THE CROSS FOR THE CROSS PLAYER AT THE CELL THAT IS SELECTED VIA THE gui
        """
        #Fits the cross inside the grid cell depending on the grid size.
        cross_x = x * (self.WIDTH + self.MARGIN)
        cross_y = y * (self.HEIGHT + self.MARGIN) + 145
        
        #Sets the width of the line to fit insice the grid cell.
        line_width = int(self.WIDTH * 0.20)
        
        #Draws two seperate lines crossing to create the cross for tic tac toe.
        pygame.draw.line(self.screen, self.RED,(cross_x + 20, cross_y + 20), (cross_x + self.WIDTH - 20, cross_y + self.HEIGHT - 20), line_width)
        pygame.draw.line(self.screen, self.RED,(cross_x + 20, cross_y + self.HEIGHT - 20), (cross_x + self.WIDTH - 20, cross_y + 20), line_width)
        pygame.display.update()

    def is_game_over(self):

        """
        YOUR CODE HERE TO SEE IF THE GAME HAS TERMINATED AFTER MAKING A MOVE. YOU SHOULD USE THE IS_TERMINAL()
        FUNCTION FROM GAMESTATUS_5120.PY FILE (YOU WILL FIRST NEED TO COMPLETE IS_TERMINAL() FUNCTION)
        
        YOUR RETURN VALUE SHOULD BE TRUE OR FALSE TO BE USED IN OTHER PARTS OF THE GAME
        """
        #Calls the is_terminal function to see if the game is over.
        return self.game_state.is_terminal()
    

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
        #Sets the depth of the search algorithms.
        depth = 4
        
        #Sets the maximizing player.
        maximizing_player = True
        turn_multiplier = 1
        
        #Sets terminal to is_terminal
        terminal = self.game_state.is_terminal()
        
        #Calls negamax search algorithm.
        if self.search == "negamax":
            result, move = negamax(self.game_state, depth, turn_multiplier)
            
        #Calls minimax search algorithm.
        else:
            result, move  = minimax(self.game_state, depth, maximizing_player)
            
        #Computes and displays scores if ai has no result.
        if result is None:
            return self.game_state.get_scores(terminal)
        
        #Computes and displays scores if ai has no moves.
        if move is None:
            return self.game_state.get_scores(terminal)
        
        #Makes the move to the cell and we assign it -1 for ai and draw the circle at that location.
        self.move(move)
        self.game_state.board_state[move[0]][move[1]] = -1
        self.draw_circle(move[0], move[1])       
        self.change_turn()
        
        #Checks if game is over with is_game_over function and if true calls is_terminal function with terminal.
        if self.is_game_over():
            """ USE self.game_state.get_scores(terminal) HERE TO COMPUTE AND DISPLAY THE FINAL SCORES """
            return self.game_state.get_scores(terminal)


    def game_reset(self):
        #Sets rows and cols to the grid size selected.
        rows = self.GRID_SIZE
        cols = self.GRID_SIZE
        
        #Iterates through every cell and assigns them to 0 to get it back to default state.
        reset_game = [[0 for i in range(rows)] for j in range(cols)]
        self.game_state = GameStatus(reset_game, True)
        
        #Redraws the grid according to the new grid size selected.
        self.WIDTH = self.size[0] / self.GRID_SIZE - self.OFFSET
        self.HEIGHT = (self.size[1] - 145) / self.GRID_SIZE - self.OFFSET
        self.draw_game()
        """
        YOUR CODE HERE TO RESET THE BOARD TO VALUE 0 FOR ALL CELLS AND CREATE A NEW GAME STATE WITH NEWLY INITIALIZED
        BOARD STATE
        """
        
        pygame.display.update()

    def play_game(self, mode = "player_vs_ai"):
        done = False

        clock = pygame.time.Clock()

        """
        YOUR CODE HERE TO CHECK IF THE USER CLICKED ON A GRID ITEM. EXIT THE GAME IF THE USER CLICKED EXIT
        """
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    """
                    YOUR CODE HERE TO NOW CHECK WHAT TO DO IF THE GAME IS NOT OVER AND THE USER SELECTED A NON EMPTY CELL
                    IF CLICKED A NON EMPTY CELL, THEN GET THE X,Y POSITION, SET ITS VALUE TO 1 (SELECTED BY HUMAN PLAYER),
                    DRAW CROSS (OR NOUGHT DEPENDING ON WHICH SYMBOL YOU CHOSE FOR YOURSELF FROM THE gui) AND CALL YOUR 
                    PLAY_AI FUNCTION TO LET THE AGENT PLAY AGAINST YOU
                    """
                #Checks if user clicked mouse.
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    
                    #Sets mouse click position to pos.
                    pos = pygame.mouse.get_pos()
                    
                    #If the mouse click occured anywhere inside where that certain button was located then it assign the 
                    # new grid size, new search algorithm, and reset the game to represent that new board.
                    if self.start_button_rect.collidepoint(pos):
                        self.game_reset()
                    elif self.three_button_rect.collidepoint(pos):
                        self.GRID_SIZE = 3
                        self.game_reset()
                    elif self.four_button_rect.collidepoint(pos):
                        self.GRID_SIZE = 4
                        self.game_reset()
                    elif self.five_button_rect.collidepoint(pos):
                        self.GRID_SIZE = 5
                        self.game_reset()
                    elif self.neg_button_rect.collidepoint(pos):
                        self.search = "negamax"
                        self.game_reset()
                    elif self.mini_button_rect.collidepoint(pos):
                        self.search = "minimax"
                        self.game_reset()
                    else:
                        #Turns the x/y screen coordinates to grid coordinates
                        grid_x = int(pos[0] // (self.WIDTH + self.MARGIN))
                        grid_y = int((pos[1] - 145) // (self.HEIGHT + self.MARGIN))
                        
                        #If the grid cell that the user clicked on is empty and is in the grid then a cross will
                        #be placed and the grid cell well be assigned the value 1 for the player.
                        if grid_y >= 0 and self.game_state.board_state[grid_x][grid_y] == 0:
                            self.game_state.board_state[grid_x][grid_y] = 1
                            self.draw_cross(grid_x, grid_y)
                            self.play_ai()
                    """
                    YOUR CODE HERE TO HANDLE THE SITUATION IF THE GAME IS OVER. IF THE GAME IS OVER THEN DISPLAY THE SCORE,
                    THE WINNER, AND POSSIBLY WAIT FOR THE USER TO CLEAR THE BOARD AND START THE GAME AGAIN (OR CLICK EXIT)
                    """
                    game_over, winner = self.is_game_over()
                    if game_over:
                        # Draw the "Winner" text on the screen
                        font = pygame.font.SysFont('Arial', 18)
                        winner_text = font.render(f'Winner: {winner}', True, self.BLACK)
                        
                        # Draw over the previous text and display the new winner text
                        pygame.draw.rect(self.screen, self.WHITE, (200, 80, 200, 30))  # Clear the previous winner text
                        self.screen.blit(winner_text, (200, 80))
                        pygame.display.update()
                        
                        # Draw the "Scores" text on the screen
                        font = pygame.font.SysFont('Arial', 18)
                        terminal = self.game_state.is_terminal()
                        scores = self.game_state.get_scores(terminal)
                        score_text = font.render(f'Scores: {scores}', True, self.BLACK)
                        
                        # Draw over the previous text and display the new scores text
                        pygame.draw.rect(self.screen, self.WHITE, (200, 120, 200, 20))  # Clear the previous winner text
                        self.screen.blit(score_text, (200, 120))
                        pygame.display.update()

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
