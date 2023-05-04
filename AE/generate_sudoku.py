import random
import numpy as np
from numba import njit
from argparse import ArgumentParser

def take_input():
    parser = ArgumentParser()
    parser.add_argument("-n", "--n", type=int, default=3)
    parser.add_argument("-o", "--output", action='store', dest='output')
    return parser

def generate_sudoku(n):
    board = [[0 for _ in range(n*n)] for _ in range(n*n)]
    rows = [set(range(1, n*n+1)) for _ in range(n*n)]
    cols = [set(range(1, n*n+1)) for _ in range(n*n)]
    boxes = [set(range(1, n*n+1)) for _ in range(n*n)]

    def box_index(row, col):
        return (row // n) * n + col // n

    def backtrack(curr):
        if curr == n*n*n*n:
            return True

        row, col = curr // (n*n), curr % (n*n)

        if board[row][col] != 0:
            return backtrack(curr + 1)

        box = box_index(row, col)
        choices = list(rows[row] & cols[col] & boxes[box])
        if not choices:
            return False

        random.shuffle(choices)
        for choice in choices:
            rows[row].remove(choice)
            cols[col].remove(choice)
            boxes[box].remove(choice)
            board[row][col] = choice

            if backtrack(curr + 1):
                return True

            rows[row].add(choice)
            cols[col].add(choice)
            boxes[box].add(choice)
            board[row][col] = 0

        return False

    backtrack(0)

    # Remove some numbers to create a puzzle
    num_cells = random.randint(n*n*2, n*n*3)
    for _ in range(num_cells):
        row, col = random.randint(0, n*n-1), random.randint(0, n*n-1)
        while board[row][col] == 0:
            row, col = random.randint(0, n*n-1), random.randint(0, n*n-1)
        board[row][col] = 0
    return board

parser = take_input()
args = parser.parse_args()
n=args.n
board = np.array(generate_sudoku(n))

@njit(fastmath=True)
def solve_sudoku(board):
    empty_cells = [(i, j) for i in range(n*n) for j in range(n*n) if board[i][j] == 0]
    idx = 0
    while idx >= 0 and idx < len(empty_cells):
        i, j = empty_cells[idx]
        found = False
        for val in range(board[i][j] + 1, n*n+1):
            if is_valid_move(board, i, j, val):
                board[i][j] = val
                idx += 1
                found = True
                break
        if not found:
            board[i][j] = 0
            idx -= 1
    return board


@njit(fastmath=True)
def is_valid_move(board, i, j, val):
    # Check row
    if val in board[i]:
        return False
    # Check column
    if val in [board[x][j] for x in range(n*n)]:
        return False
    # Check 3x3 subgrid
    sub_i, sub_j = i // n * n, j // n * n
    if val in [board[sub_i + m][sub_j + o] for m in range(n) for o in range(n)]:
        return False
    return True

print(board)
print(solve_sudoku(board))