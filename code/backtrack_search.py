def next_empty(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                return (row, col)

    return None

def is_valid_move(grid, row, col):
    return None

def backtrack_solve(grid):
    return None