from Test_GameStatus import GameStatus 

def minimax(game_state: GameStatus, depth: int, maximizingPlayer: bool, alpha=float('-inf'), beta=float('inf')):
    terminal = game_state.is_terminal()
    if (depth == 0) or (terminal[0]):  # Check if the game has ended or if depth is 0
        newScores = game_state.get_scores(terminal)  # Set the score for the terminal state
        return newScores, None  # Return the scores and None (as best move)
    
    best_move = None
    
    if maximizingPlayer:
        bestVal = float('-inf')  # Set default value to negative infinity
        moves = game_state.get_moves()  # Get available moves (empty cells)
        for move in moves:
            new_game_state = game_state.get_new_state(move)  # Generate new state with this move
            value, _ = minimax(new_game_state, depth - 1, False, alpha, beta)  # Recursively call minimax on the new state
            if value > bestVal:  # If this value is better, update best value and move
                bestVal = value
                best_move = move
            alpha = max(alpha, bestVal)  # Update alpha value
            if beta <= alpha:  # Alpha-beta pruning condition
                break
        return bestVal, best_move

    else:  # Minimizing player
        bestVal = float('inf')  # Set default value to positive infinity
        moves = game_state.get_moves()  # Get available moves (empty cells)
        for move in moves:
            new_game_state = game_state.get_new_state(move)  # Generate new state with this move
            value, _ = minimax(new_game_state, depth - 1, True, alpha, beta)  # Recursively call minimax on the new state
            if value < bestVal:  # If this value is better (lower), update best value and move
                bestVal = value
                best_move = move
            beta = min(beta, bestVal)  # Update beta value
            if beta <= alpha:  # Alpha-beta pruning condition
                break
        return bestVal, best_move

    """
    YOUR CODE HERE TO FIRST CHECK WHICH PLAYER HAS CALLED THIS FUNCTION (MAXIMIZING OR MINIMIZING PLAYER)
    YOU SHOULD THEN IMPLEMENT MINIMAX WITH ALPHA-BETA PRUNING AND RETURN THE FOLLOWING TWO ITEMS
    1. VALUE
    2. BEST_MOVE
    
    THE LINE TO RETURN THESE TWO IS COMMENTED BELOW WHICH YOU CAN USE
    """

def negamax(game_state: GameStatus, depth: int, turn_multiplier: int, alpha=float('-inf'), beta=float('inf')):
    terminal = game_state.is_terminal()
    if (depth == 0) or (terminal[0]):  # Check if the game has ended or if depth is 0
        scores = game_state.get_negamax_scores(terminal)  # Set the score for the terminal state
        return scores * turn_multiplier, None  # Return the scores adjusted for turn_multiplier
    
    best_move = None
    bestVal = float('-inf')  # Set default value to negative infinity
    moves = game_state.get_moves()  # Get available moves (empty cells)
    
    for move in moves:
        new_game_state = game_state.get_new_state(move)  # Generate new state with this move
        value, _ = negamax(new_game_state, depth - 1, -turn_multiplier, -beta, -alpha)  # Recursively call negamax with flipped turn_multiplier
        value = -value  # Negate the returned value
        if value > bestVal:  # If this value is better, update best value and move
            bestVal = value
            best_move = move
        alpha = max(alpha, bestVal)  # Update alpha value
        if alpha >= beta:  # Alpha-beta pruning condition
            break
    return bestVal, best_move
    

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