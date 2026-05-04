"""
Run round-robin between each 5 variants against each other
for 100 games. Record number of wins per alg., 25 combinations total
Prints a win %
"""

from board import get_legal_moves, make_move, is_terminal, other_player
from algorithms.ur    import uniform_random
from algorithms.pmcgs import pmcgs
from algorithms.uct   import uct

AGENTS = [
    ("UR",           lambda b, p: uniform_random(b, p)),
    ("PMCGS(500)",   lambda b, p: pmcgs(b, p, 500,   "None")),
    ("PMCGS(10000)", lambda b, p: pmcgs(b, p, 10000, "None")),
    ("UCT(500)",     lambda b, p: uct(b,  p, 500,    "None")),
    ("UCT(10000)",   lambda b, p: uct(b,  p, 10000,  "None")),
]

#create empty board for the start of the game
def empty_board():
    return [['0'] * 7 for _ in range(6)]

#plays full game between two agents, sequential moves
#checks is_terminal after each move
def play_game(agent_y, agent_r):
    board = empty_board()
    current = 'Y'
    while True:
        agent = agent_y if current == 'Y' else agent_r
        col = agent(board, current)
        row = make_move(board, col, current)
        result = is_terminal(board, col - 1, row)
        if result is not None:
            return 'Y' if result == 1 else ('R' if result == -1 else 'D')
        current = other_player(current)

#round robin tournament for 100 games per pair of agents
def run_tournament(games_per_pair = 100):
    wins = [[0] * len(AGENTS) for _ in range(len(AGENTS))]
    for i, (name_i, agent_i) in enumerate(AGENTS):
        for j, (name_j, agent_j) in enumerate(AGENTS):
            w = 0
            for _ in range(games_per_pair):
                result = play_game(agent_i, agent_j)
                if result == 'Y':
                    w += 1
            wins[i][j] = w
            pct = 100 * w / games_per_pair
            print(f"  {name_i:15s} vs {name_j:15s} → {w}/{games_per_pair} ({pct:.1f}%)")
    return wins

#prints tournament results in a table format
def print_table(wins, games_per_pair = 100):
    names = [a[0] for a in AGENTS]
    col_w = 13
    print("\n" + " " * 16 + "".join(f"{n:>{col_w}}" for n in names))
    print("-" * (16 + col_w * len(names)))
    for i, name_i in enumerate(names):
        row = f"{name_i:<16}"
        for j in range(len(names)):
            pct = 100 * wins[i][j] / games_per_pair
            row += f"{pct:>{col_w}.1f}%"
        print(row)
if __name__ == "__main__":
    wins = run_tournament()
    print_table(wins)
