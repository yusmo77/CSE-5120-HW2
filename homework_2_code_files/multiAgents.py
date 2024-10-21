from GameStatus_5120 import GameStatus 
import pdb

def minimax(game_state: GameStatus, depth: int, maximizingPlayer: bool, latest_move: int, alpha=float('-inf'), beta=float('inf')):
    terminal = game_state.is_terminal() 
    if (depth==0) or (terminal[0]): #Check if the game has ended or if depth is 0
        #newScores = game_state.get_scores(terminal) #If so, sets the score
        newScores, _, _ = game_state.grade_board_state()
        return newScores, None   #Return the scores and None (as best move)

    if maximizingPlayer:
        bestVal = float('-inf')  #Sets default value to negative infinity, which is worst case scenerio
        best_move = None         # Sets default best move to None
        children, children_positions = game_state.get_children(maximizingPlayer, latest_move)
        for position, child in enumerate(children): #Iterates through the children of the game state
            value, _ = minimax(child, depth - 1, False, latest_move, alpha, beta) #Recursively calls minimax on the child
            if value > bestVal:   #If the value is greater than the best value
                bestVal = value   # Then value replaces the prev. best (highest) value
                best_move = children_positions[position] #Sets the best move equal to the current node
            alpha = max(alpha, bestVal) #Sets alpha equal to either alpha or bestVal depending on whichever is greater
            if beta <= alpha:     # Error Handling: If alpha is equal to infinity, something went wrong
                break
    else:                         #If the player is minimizing
        bestVal = float('inf')    #Sets default value to positive infinity, which is worst case scenerio
        best_move = None          # Sets default best move to None
        children, children_positions = game_state.get_children(maximizingPlayer, latest_move)
        for position, child in enumerate(children): #Iterates through the children of the game state
            value, _ = minimax(child, depth - 1, True, latest_move, alpha, beta) #Recursively calls minimax on the child
            if value < bestVal:   #If the value is less than the best value
                bestVal = value   # Then value replaces the prev. best (lowest) value
                best_move = children_positions[position] #Sets the best move equal to the current node
            beta = min(beta, bestVal) #Sets beta equal to either beta or bestVal depending on whichever is smaller
            if beta <= alpha:     # Error Handling: If beta is less than alpha, something went wrong
                break

    """
    YOUR CODE HERE TO FIRST CHECK WHICH PLAYER HAS CALLED THIS FUNCTION (MAXIMIZING OR MINIMIZING PLAYER)
    YOU SHOULD THEN IMPLEMENT MINIMAX WITH ALPHA-BETA PRUNING AND RETURN THE FOLLOWING TWO ITEMS
    1. VALUE
    2. BEST_MOVE
    
    THE LINE TO RETURN THESE TWO IS COMMENTED BELOW WHICH YOU CAN USE
    """
    return value, best_move #Returns the value and the best move (value and best move depend on which player called the function, either maximizing or minimizing)

def negamax(game_status: GameStatus, depth: int, turn_multiplier: int, latest_move: int, alpha=float('-inf'), beta=float('inf')):
    #pdb.set_trace()
    terminal = game_status.is_terminal()
    if (depth==0) or (terminal[0]):#Check if the game has ended or if depth is 0
        scores, _, _ = game_status.grade_board_state()#If so, sets the score
        return scores, None     #Return the scores and None (as best move)
    score = float('-inf')       #Sets default value to negative infinity, which is worst case scenerio
    best_move = None            # Sets default best move to None

    children, children_positions = game_status.get_children(turn_multiplier, latest_move)
    for position, child in enumerate(children): #Iterates through the children of the game state
        value, _ = negamax(child, depth - 1, -turn_multiplier, latest_move, -beta, -alpha) #Recursively calls negamax on the child
                                                                              #Negamax is called with the negative of the beta, alpha values, and turn_multiplier
        value = -value          #Negates the value
        if value > score:       #If the value is greater than the best value
            score = value       # Then value replaces the prev. best (highest) value
            best_move = children_positions[position]  #Sets the best move equal to the current node
        
        if turn_multiplier == 1:
            alpha = max(alpha,score)
            if beta <= alpha:
                break
        else:
            beta = min(beta,score)
            if beta <= alpha:
                break
            
    return score, best_move   #Returns the value and the best move
    

    """
    YOUR CODE HERE TO CALL NEGAMAX FUNCTION. REMEMBER THE RETURN OF THE NEGAMAX SHOULD BE THE OPPOSITE OF THE CALLING
    PLAYER WHICH CAN BE DONE USING -NEGAMAX(). THE REST OF YOUR CODE SHOULD BE THE SAME AS MINIMAX FUNCTION.
    YOU ALSO DO NOT NEED TO TRACK WHICH PLAYER HAS CALLED THE FUNCTION AND SHOULD NOT CHECK IF THE CURRENT MOVE
    IS FOR MINIMAX PLAYER OR NEGAMAX PLAYER
    RETURN THE FOLLOWING TWO ITEMS
    1. VALUE
    2. BEST_MOVE
    
    THE LINE TO RETURN THESE TWO IS COMMENTED BELOW WHICH YOU CAN USE
    
    """
