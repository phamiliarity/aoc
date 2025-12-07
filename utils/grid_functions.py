def transpose(grid):
    return [list(row) for row in zip(*grid)]

def find_first_char(grid, char):
    m = len(grid)
    n = len(grid[0])
    return next(((ii, jj) for ii in range(m)
                 for jj in range(n) if grid[ii][jj] == char), None)

def get_8neighbours(ii, jj, grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    return [
        (ni, nj)
        for ni in range(ii - 1, ii + 2)
        for nj in range(jj - 1, jj + 2)
        if (ni, nj) != (ii, jj) and 0 <= ni < rows and 0 <= nj < cols
    ]

def print_grid(grid):
    print("\n".join(map(str, grid)))
