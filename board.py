#checks if top row of each column is open '0'
def get_legal_moves(board):
    legal_moves = []
    for col in range(7):
        if board[0][col] == "O":
            legal_moves.append(col + 1)
    return legal_moves

#check what row of the column is open to make player's move
def make_move(board, col, player):
    for row in range(5, -1, -1):
        if board[row][col - 1] == 'O':
            board[row][col - 1] = player
            return row

#sets cell back to '0'
def undo_move(board, col, row):
    board[row][col - 1] = 'O'

# col and row are 0-indexed. Returns 1 (Y wins), -1 (R wins), 0 (draw), None (ongoing).
def is_terminal(board, col, row):
    player = board[row][col]
    for dr, dc in [(0, 1), (1, 0), (1, 1), (1, -1)]:
        count = 1
        r, c = row + dr, col + dc
        while 0 <= r < 6 and 0 <= c < 7 and board[r][c] == player:
            count += 1
            r += dr
            c += dc
        r, c = row - dr, col - dc
        while 0 <= r < 6 and 0 <= c < 7 and board[r][c] == player:
            count += 1
            r -= dr
            c -= dc
        if count >= 4:
            return 1 if player == 'Y' else -1
    for c in range(7):
        if board[0][c] == 'O':
            return None
    return 0
