import numpy as np
from time import time
from argparse import ArgumentParser


def input():
    parser = ArgumentParser()
    parser.add_argument("-n", "--n", type=int, default=3)
    parser.add_argument("-o", "--output", action='store', dest='output')
    return parser

parser = input()
args = parser.parse_args()
n=args.n

if n==2:
    board = np.array([
    [3, 0, 0, 0],
    [0, 4, 0, 0],
    [4, 0, 0, 3],
    [0, 0, 1, 4]
    ])
elif n==3:
    board =np.array([
    [9, 6, 2, 0, 7, 4, 5, 0, 1],
    [7, 0, 8, 5, 6, 0, 3, 2, 9],
    [3, 1, 5, 2, 8, 9, 7, 4, 6],
    [0, 3, 7, 9, 0, 2, 0, 1, 0],
    [0, 9, 1, 8, 0, 0, 4, 3, 0],
    [0, 8, 4, 1, 3, 6, 9, 5, 7],
    [1, 0, 3, 6, 0, 5, 8, 9, 4],
    [4, 5, 9, 7, 1, 8, 0, 6, 0],
    [8, 2, 6, 4, 9, 3, 1, 7, 0]
    ])
elif n==4:
    board = np.array([
    [11, 13, 14, 10, 12, 15, 9, 5, 7, 2, 8, 6, 4, 3, 1, 16],
    [15, 4, 1, 7, 10, 0, 0, 16, 5, 13, 9, 3, 0, 8, 12, 6],
    [2, 0, 6, 0, 13, 3, 7, 1, 4, 12, 11, 16, 5, 10, 15, 0],
    [0, 5, 16, 3, 6, 4, 11, 8, 1, 15, 10, 14, 0, 13, 7, 9],
    [5, 10, 15, 14, 16, 8, 1, 7, 6, 11, 13, 4, 12, 2, 9, 3],
    [7, 2, 9, 12, 14, 13, 4, 0, 16, 1, 3, 8, 10, 5, 6, 11],
    [6, 0, 13, 11, 9, 12, 2, 0, 15, 5, 14, 10, 8, 0, 16, 4],
    [8, 0, 4, 16, 5, 0, 10, 11, 9, 7, 2, 0, 13, 1, 14, 15],
    [16, 15, 8, 4, 7, 11, 3, 14, 13, 0, 5, 1, 6, 12, 0, 2],
    [3, 7, 5, 9, 15, 1, 8, 0, 14, 10, 12, 2, 16, 11, 4, 13],
    [10, 6, 2, 1, 4, 9, 13, 12, 8, 16, 7, 0, 0, 15, 3, 5],
    [0, 11, 12, 13, 2, 16, 5, 10, 3, 0, 0, 15, 1, 9, 8, 0],
    [13, 14, 10, 5, 8, 7, 16, 4, 0, 3, 1, 0, 15, 0, 0, 12],
    [4, 12, 11, 6, 3, 5, 15, 2, 10, 8, 16, 7, 9, 14, 13, 1],
    [9, 8, 3, 2, 1, 14, 6, 0, 12, 0, 0, 5, 7, 16, 11, 10],
    [1, 0, 7, 0, 11, 10, 12, 9, 0, 0, 6, 13, 3, 4, 5, 8]
    ])



def solve_sudoku_b(board):
    # find an empty cell
    for i in range(n*n):
        for j in range(n*n):
            if board[i][j] == 0:
                # try out numbers 1 to 9
                for num in range(1, n*n+1):
                    # check if number is valid
                    if is_valid(board, i, j, num):
                        # place number in cell
                        board[i][j] = num
                        # move to next cell
                        if solve_sudoku_b(board):
                            return True
                        # backtrack if solution is invalid
                        board[i][j] = 0
                # if all numbers are tried and none are valid, backtrack
                return False
    # if there are no empty cells left, the puzzle is solved
    return True

def is_valid(board, row, col, num):
    # check row
    for j in range(n*n):
        if board[row][j] == num:
            return False
    # check column
    for i in range(n*n):
        if board[i][col] == num:
            return False
    # check 3x3 sub-grid
    sub_row = (row // n) * n
    sub_col = (col // n) * n
    for i in range(sub_row, sub_row + n):
        for j in range(sub_col, sub_col + n):
            if board[i][j] == num:
                return False
    return True

t0 = time()
p = solve_sudoku_b(board)
t1 = time()
print(t1-t0)