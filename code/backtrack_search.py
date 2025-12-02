import math

GRID_DIMENSIONS = 9
SUBGRID_DIMENSIONS = int(math.sqrt(GRID_DIMENSIONS))

count = 0

def next_empty(grid):
    for row in range(GRID_DIMENSIONS):
        for col in range(GRID_DIMENSIONS):
            if grid[row][col] == 0:
                return (row, col)

    return None

def is_valid_move(grid, row, col, num):
    for i in range(GRID_DIMENSIONS):
        if grid[row][i] == num:
            return False

    for i in range(GRID_DIMENSIONS):
        if grid[i][col] == num:
            return False

    start_row = row - (row % SUBGRID_DIMENSIONS)
    start_col = col - (col % SUBGRID_DIMENSIONS)

    for i in range(SUBGRID_DIMENSIONS):
        for j in range(SUBGRID_DIMENSIONS):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

def backtrack_solve(grid):
    global count
    count += 1
    empty = next_empty(grid)
    if empty is None:
        return True

    row, col = empty

    for num in range(1, GRID_DIMENSIONS + 1):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if backtrack_solve(grid):
                return True

            grid[row][col] = 0

    return False

if __name__ == '__main__':
    grid = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    if backtrack_solve(grid):
        for row in grid:
            print(row)
    else:
        print("No solution")

    print(count)