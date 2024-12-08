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

def calc_antinode_coords(coord1, coord2):
    dr = coord1[0] - coord2[0]
    dc = coord1[1] - coord2[1]

    antinode1 = (coord1[0] + dr, coord1[1] + dc)
    antinode2 = (coord2[0] - dr, coord2[1] - dc)
    return antinode1, antinode2

grid = list(map(list, open("input.txt").read().splitlines()))
n,m = len(grid), len(grid[0])

antenna_coords = get_all_antenna_coords(grid)

antinode_coords = set()
for antenna, coords in antenna_coords.items():
    for idx, coord1 in enumerate(coords):
        for coord2 in coords[idx+1:]:
            antinode1, antinode2 = calc_antinode_coords(coord1, coord2)

            for antinode in calc_antinode_coords(coord1, coord2):
                #stay in grid
                if -1 < antinode[0] < n and -1 < antinode[1] < m:
                    antinode_coords.add(antinode)
print(len(antinode_coords))