def get_8neighbours(ii, jj, grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    return [
        (ni, nj)
        for ni in range(ii - 1, ii + 2)
        for nj in range(jj - 1, jj + 2)
        if (ni, nj) != (ii, jj) and 0 <= ni < rows and 0 <= nj < cols
    ]

grid = open("input.txt").read().split(("\n"))
for idx, g in enumerate(grid):
    grid[idx] = list(g)
i = len(grid)
j = len(grid[0])

ans = 0

while True:
    removed = []
    for ii in range(i):
        for jj in range(j):
            if grid[ii][jj] == "@":
                ns = get_8neighbours(ii, jj, grid)
                sym_ns = [grid[nn[0]][nn[1]] for nn in ns]
                if sym_ns.count("@") < 4:
                    removed.append((ii, jj))

    if not removed:
        break

    ans += len(removed)
    for (iii, jjj) in removed:
        grid[iii][jjj] = "x"

print(ans)