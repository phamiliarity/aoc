def get_8neighbours(ii, jj, grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    return [
        (ni, nj)
        for ni in range(ii - 1, ii + 2)
        for nj in range(jj - 1, jj + 2)
        if (ni, nj) != (ii, jj) and 0 <= ni < rows and 0 <= nj < cols
    ]

def transpose(grid):
    return [list(row) for row in zip(*grid)]
    