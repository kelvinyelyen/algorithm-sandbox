def print_solution(board):
    N = len(board)
    for i in range(N):
        for j in range(N):
            print("Q" if board[i][j] == 1 else ".", end=" ")
        print()
    print("-" * (2 * N))

def is_safe(board, row, col):
    N = len(board)

    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col):
    N = len(board)
    
    # base case: If all queens are placed then return true
    if col >= N:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # recur to place rest of the queens
            if solve_n_queens_util(board, col + 1):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove queen from board[i][col]
            board[i][col] = 0

    return False

def solve_n_queens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solve_n_queens_util(board, 0):
        print("Solution does not exist")
        return False

    print(f"Solution for N={N}:")
    print_solution(board)
    return True

if __name__ == "__main__":
    solve_n_queens(4)
    solve_n_queens(8)
