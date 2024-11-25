

with open("inputs/p096_sudoku.txt", "r") as f:
    lines = f.readlines()

sudoku = []
for i in range(0, len(lines), 10):
    board = []
    for j in range(i+1, i+10):
        board.append(list(map(int, lines[j].strip())))
    sudoku.append(board)

    # for line in board:
    #     print(line)
    # print()

def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for k in range(1, 10):
                    if k not in board[i] and k not in [board[x][j] for x in range(9)] and k not in [board[x][y] for x in range(i//3*3, i//3*3+3) for y in range(j//3*3, j//3*3+3)]:
                        board[i][j] = k
                        if solve(board):
                            return True
                        board[i][j] = 0
                return False
    return True

total = 0
for i, board in enumerate(sudoku):
    solve(board)
    total += board[0][0]*100 + board[0][1]*10 + board[0][2]

    print(f"Solved: {i}")

print(total)