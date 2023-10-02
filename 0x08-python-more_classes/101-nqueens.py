#!/usr/bin/python3
"""Solves the N-queens puzzle."""

import sys

def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at a given position on the board.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row to check.
        col (int): The column to check.
        N (int): The size of the chessboard.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    for i in range(row):
        # Check the column
        if board[i][col] == 'Q':
            return False

        # Check the upper-left diagonal
        if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
            return False

        # Check the upper-right diagonal
        if col + (row - i) < N and board[i][col + (row - i)] == 'Q':
            return False

    return True

def solve_nqueens(N):
    """
    Solve the N-Queens puzzle and print all solutions.

    Args:
        N (int): The size of the chessboard.

    Raises:
        SystemExit: Exits the program if input conditions are not met.
    """
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [['.' for _ in range(N)] for _ in range(N)]

    def get_solution(board):
        """
        Extract the solution from the chessboard in the specified format.

        Args:
            board (list): The current state of the chessboard.

        Returns:
            list: A list of lists representing the queen positions.
        """
        solution = []
        for r in range(N):
            for c in range(N):
                if board[r][c] == 'Q':
                    solution.append([r, c])
        return solution

    def solve(row):
        """
        Recursively find and print all solutions to the N-Queens puzzle.

        Args:
            row (int): The current row being considered.

        Returns:
            None
        """
        if row == N:
            solution = get_solution(board)
            print(solution)
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 'Q'
                solve(row + 1)
                board[row][col] = '.'

    solve(0)

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
