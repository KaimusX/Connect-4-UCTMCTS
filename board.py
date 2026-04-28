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
