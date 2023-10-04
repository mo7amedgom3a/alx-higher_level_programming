import sys

def is_safe(board, row, col, N):
    # Check if the current position is safe for the queen
    # across the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens_util(board, row, N, solutions):
    # Base case: If all queens are placed, add the solution to the solutions list
    if row == N:
        solutions.append(board[:])
        return

    # Try placing the queen in each column of the current row
    for col in range(N):
        if is_safe(board, row, col, N):
            # Place the queen
            board[row][col] = 1

            # Recur for the next row
            solve_n_queens_util(board, row + 1, N, solutions)

            # Backtrack and remove the queen
            board[row][col] = 0


def solve_n_queens(N):
    solutions = []
    board = [[0] * N for _ in range(N)]
    solve_n_queens_util(board, 0, N, solutions)
    return solutions


def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print(" ".join("Q" if cell == 1 else "-" for cell in row))
        print()


def main():
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get N from the command-line argument
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is valid
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(N)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
