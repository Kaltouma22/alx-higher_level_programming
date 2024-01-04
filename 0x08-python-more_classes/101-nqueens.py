#!/usr/bin/python3

import sys


def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(N):
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]

    def solve_util(board, col):
        if col == N:
            for row in board:
                print(' '.join(map(str, row)))
            print()
            return True

        res = False
        for i in range(N):
            if is_safe(board, i, col, N):
                board[i][col] = 1
                res = solve_util(board, col + 1) or res
                board[i][col] = 0

        return res

    if not solve_util(board, 0):
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
