import math

def print_board(board):
    for row in board:
        print("| " + " | ".join(row) + " |")

def check_winner(board):
    # Έλεγχος γραμμών, στηλών και διαγωνίων
    win_states = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    if ["X", "X", "X"] in win_states: return "X"
    if ["O", "O", "O"] in win_states: return "O"
    if all(cell != " " for row in board for cell in row): return "Tie"
    return None

def minimax(board, depth, is_maximizing):
    res = check_winner(board)
    if res == "X": return -10
    if res == "O": return 10
    if res == "Tie": return 0

    if is_maximizing:
        best_score = -math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = "O"
                    score = minimax(board, depth + 1, False)
                    board[r][c] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = "X"
                    score = minimax(board, depth + 1, True)
                    board[r][c] = " "
                    best_score = min(score, best_score)
        return best_score

# Απλοποιημένη έκδοση για να δεις την κίνηση της AI
board = [
    ["X", "O", "X"],
    [" ", "O", " "],
    [" ", " ", "X"]
]

print("Current Board:")
print_board(board)
print("\nΗ AI (O) σκέφτεται την καλύτερη κίνηση...")
# Εδώ θα έμπαινε η λογική για να παίξει η AI
