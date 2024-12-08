def get_all_antenna_coords(grid):
    n,m = len(grid), len(grid[0])

    frequencies = list(set("".join("".join(r) for r in grid)))
    frequencies.remove(".")

    antenna_coords = {frequency : [] for frequency in frequencies}

    for r in range(n):
        for c in range(m):
            char = str(grid[r][c])
            if char != ".":
                antenna_coords[char].append((r,c))
    return antenna_coords

def calc_antinode_coords(coord1, coord2, n, m):
    antinodes = []
    dr = coord1[0] - coord2[0]
    dc = coord1[1] - coord2[1]

    #calculate until out of bounds
    for direction in (1, -1):
        i = 1
        while True:
            antinode = (coord1[0] + direction * dr * i, coord1[1] + direction * dc * i)
            if not (-1 < antinode[0] < n or -1 < antinode[1] < m):
                break
            antinodes.append(antinode)
            i += 1

    return antinodes

grid = list(map(list, open("input.txt").read().splitlines()))
n,m = len(grid), len(grid[0])

antenna_coords = get_all_antenna_coords(grid)

antinode_coords = set()
n_match2 = 0
for antenna, coords in antenna_coords.items():
    for idx, coord1 in enumerate(coords):
        for coord2 in coords[:idx] + coords[idx+1:]:

            for antinode in calc_antinode_coords(coord1, coord2, n, m):
                #stay in grid
                if -1 < antinode[0] < n and -1 < antinode[1] < m:
                    antinode_coords.add(antinode)

print(len(antinode_coords))