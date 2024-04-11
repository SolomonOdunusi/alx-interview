#!/usr/bin/python3
"""
N-Queens Puzzle
"""
import sys


def printSolution(board):
    """Print the coordinates row and col for the position of
       each N queen in the posible solution
    """
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


def getCandidates(board, row, col, n):
    """
    Checks if a queen can be placed on board[row][col]
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQueens(board, col, n):
    """Solves the N Queen problem using backtracking"""
    if col == n:
        printSolution(board)
        return True

    counter = False
    for i in range(n):
        if getCandidates(board, i, col, n):
            board[i][col] = 1
            counter = solveNQueens(board, col + 1, n) or counter
            board[i][col] = 0
    return counter


if __name__ == "__main__":
    """
    Main function to solve N Queen Problem
    """
    if not len(sys.argv) == 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if not (sys.argv[1]).isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for i in range(n)] for j in range(n)]
    solveNQueens(board, 0, n)
