def next_empty(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                return (row, col)

    return None

def is_valid_move(grid, row, col, num):
    return None

def backtrack_solve(grid):
    empty = next_empty(grid)
    if empty is None:
        return True

    row, col = empty

    for num in range(1, len(grid)):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if backtrack_solve(grid):
                return True

            grid[row][col] = 0

    return False