from algorithms.mcts import mcts_select_move

def uct(board, player, num_simulations, output_mode):
    """Upper Confidence Bounds for Trees - UCB selection when all children explored"""
    return mcts_select_move(board, player, num_simulations, output_mode, use_ucb = True)
