import random
from board import get_legal_moves

# Gets list of legal moves, randomly picks one.
def uniform_random(board, player):
    legal_moves = get_legal_moves(board)

    if not legal_moves:
        return None
    
    return random.choice(legal_moves)