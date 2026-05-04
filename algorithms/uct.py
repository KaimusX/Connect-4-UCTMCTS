import math
import random
from board import get_legal_moves, make_move, undo_move, is_terminal
from node import TreeNode
 
 
def _other(player):
    return 'Y' if player == 'R' else 'R'
 
 
def _rollout(board, player, output_mode):
    moves_made = []
    current = player
    result = 0
    while True:
        legal = get_legal_moves(board)
        if not legal:
            result = 0
            break
        col = random.choice(legal)
        row = make_move(board, col, current)
        moves_made.append((col, row))
        if output_mode == "Verbose":
            print(f"Move selected: {col}")
        result = is_terminal(board, col - 1, row)
        if result is not None:
            break
        current = _other(current)
    for col, row in reversed(moves_made):
        undo_move(board, col, row)
    return result
 
 
def _ucb_select(node, legal, player, C=math.sqrt(2)):
    best_col = None
    best_val = None
    for col in legal:
        child = node.children[col]
        exploit = child.wi / child.ni
        explore = C * math.sqrt(math.log(node.ni) / child.ni)
        val = exploit + explore if player == 'Y' else exploit - explore
        if best_val is None or val > best_val:
            best_val = val
            best_col = col
    return best_col
 
 
def uct(board, player, num_simulations, output_mode):
    root = TreeNode()
 
    for _ in range(num_simulations):
        node = root
        path = [(node, None, None)]  # (node, col, row)
        current_player = player
        terminal_result = None
 
        while True:
            legal = get_legal_moves(board)
 
            if not legal:
                terminal_result = 0
                break
 
            unexplored = [c for c in legal if c not in node.children]
 
            if output_mode == "Verbose":
                print(f"wi: {node.wi}")
                print(f"ni: {node.ni}")
 
            if unexplored:
                # Expansion: pick a random unexplored child
                col = random.choice(unexplored)
                if output_mode == "Verbose":
                    print(f"Move selected: {col}")
                row = make_move(board, col, current_player)
                terminal_result = is_terminal(board, col - 1, row)
 
                new_node = TreeNode(parent=node)
                node.children[col] = new_node
                node = new_node
                path.append((node, col, row))
                current_player = _other(current_player)
 
                if output_mode == "Verbose":
                    print("NODE ADDED")
 
                if terminal_result is None:
                    terminal_result = _rollout(board, current_player, output_mode)
 
                if output_mode == "Verbose":
                    print(f"TERMINAL NODE VALUE: {terminal_result}")
                break
            else:
                # Selection: all children explored, use UCB
                col = _ucb_select(node, legal, current_player)
                if output_mode == "Verbose":
                    print(f"Move selected: {col}")
                row = make_move(board, col, current_player)
                terminal_result = is_terminal(board, col - 1, row)
                node = node.children[col]
                path.append((node, col, row))
                current_player = _other(current_player)
 
                if terminal_result is not None:
                    if output_mode == "Verbose":
                        print(f"TERMINAL NODE VALUE: {terminal_result}")
                    break
 
        # Backpropagate innermost to root
        for i in range(len(path) - 1, -1, -1):
            n, col, row = path[i]
            n.wi += terminal_result
            n.ni += 1
            if output_mode == "Verbose":
                print("Updated values:")
                print(f"wi: {n.wi}")
                print(f"ni: {n.ni}")
            if col is not None:
                undo_move(board, col, row)
 
    # Column summary
    if output_mode != "None":
        for col in range(1, 8):
            if col in root.children and root.children[col].ni > 0:
                val = root.children[col].wi / root.children[col].ni
                print(f"Column {col}: {val}")
            else:
                print(f"Column {col}: Null")
 
    # Select best move by wi/ni (not UCB)
    legal = get_legal_moves(board)
    best_col = None
    best_val = None
    for col in legal:
        if col in root.children and root.children[col].ni > 0:
            val = root.children[col].wi / root.children[col].ni
            if best_col is None:
                best_col = col
                best_val = val
            elif player == 'Y' and val > best_val:
                best_col = col
                best_val = val
            elif player == 'R' and val < best_val:
                best_col = col
                best_val = val
 
    if best_col is None:
        best_col = random.choice(legal) if legal else None
 
    return best_col
 
