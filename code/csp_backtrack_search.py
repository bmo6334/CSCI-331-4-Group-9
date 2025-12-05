import math
import time

GRID_DIMENSIONS = 9
SUBGRID_DIMENSIONS = int(math.sqrt(GRID_DIMENSIONS))

neighbors = {}
count = 0

def find_neighbors():
    neighbors = {}

    for row in range(GRID_DIMENSIONS):
        for col in range(GRID_DIMENSIONS):
            set_neighbors = set()

            subgrid_row = row - (row % SUBGRID_DIMENSIONS)
            subgrid_col = col - (col % SUBGRID_DIMENSIONS)

            for r in range(subgrid_row, subgrid_row + SUBGRID_DIMENSIONS):
                for c in range(subgrid_col, subgrid_col + SUBGRID_DIMENSIONS):
                    if (r, c) != (row, col):
                        set_neighbors.add((r, c))

            for r in range(GRID_DIMENSIONS):
                if r != row:
                    set_neighbors.add((r, col))

            for c in range(GRID_DIMENSIONS):
                if c != col:
                    set_neighbors.add((row, c))

            neighbors[(row, col)] = set_neighbors

    return neighbors

def find_values(grid):
    values = {}

    for row in range(GRID_DIMENSIONS):
        for col in range(GRID_DIMENSIONS):
            set_values = set()
            
            if grid[row][col] == 0:
                for i in range(1, GRID_DIMENSIONS + 1):
                    if is_valid_move(grid, row, col, i):
                        set_values.add(i)
            else:
                set_values.add(grid[row][col])
            values[(row, col)] = set_values

    return values


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


def forward_check_solve(grid, values, neighbors):
    global count
    count += 1
    empty = next_empty(grid)
    if empty is None:
        return True

    row, col = empty

    for num in values[(row, col)]:
        grid[row][col] = num

        removed = []
        valid = True

        for neighbor in neighbors[(row, col)]:
            if num in values[neighbor]:
                values[neighbor].remove(num)
                removed.append((neighbor, num))

                if not values[neighbor]:
                    valid = False
                    break

        if valid:
            if forward_check_solve(grid, values, neighbors):
                return True

        for (neighbor, num) in removed:
            values[neighbor].add(num)

        grid[row][col] = 0

    return False


if __name__ == '__main__':
    grid = [
        [4, 2, 0, 0, 8, 0, 0, 0, 7],
        [3, 0, 0, 0, 0, 6, 0, 0, 2],
        [0, 0, 0, 0, 0, 5, 0, 0, 4],
        [2, 0, 0, 0, 0, 8, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 7, 0, 0, 0, 0, 3],
        [8, 0, 0, 0, 0, 9, 0, 1, 0],
        [0, 0, 9, 0, 5, 0, 0, 3, 0],
        [0, 5, 4, 0, 0, 0, 0, 0, 0]
    ]

    start = time.time_ns()
    end = 0

    neighbors = find_neighbors()
    values = find_values(grid)

    if forward_check_solve(grid, values, neighbors):
        end = time.time_ns()
        for row in grid:
            print(row)
    else:
        print("No solution")

    print(f"Count: {count}")
    print(f"Time: {(end - start) / 1000000: .3f} ms")