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
i = len(grid)
j = len(grid[0])

ans = 0

for ii in range(i):
    for jj in range(j):

        if grid[ii][jj] == "@":
            ns = get_8neighbours(ii, jj, grid)

            sym_ns = [grid[nn[0]][nn[1]] for nn in ns]
            if sym_ns.count("@") < 4:
                ans += 1
                
print(ans)

# actually not the proper way, as the code doesnt only look at the outside
# positions, but at internal coords as well, even if it cannot be accessed
# seems like it doesnt matter though for the aoc input.
# would be nice to revisit with a pathfinding approach some day!
