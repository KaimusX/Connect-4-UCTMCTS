import random

# Gets list of legal moves, randomly picks one.
def uniform_random(board, player):
    legal_moves = get_legal_moves(board)

    if not legal_moves:
        return None
    
    return random.choice(legal_moves)

def get_legal_moves(board):
    legal_moves = []

    for col in range(7):
        # There is space in top row.
        if board[0][col] == "0":
            legal_moves.append(col + 1)

    return legal_moves