DIRECTIONS = {"^":(-1,0), ">":(0,1), "v":(1,0), "<":(0,-1)}

def get_positions_of_char(grid, char):
    """get coords of a character in a grid"""
    pos = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == char:
                pos.append((i,j))
    return pos

def detect_in_front(grid, spots_in_front, current_i, current_j, di, dj):
    """get elements in front of robot until a free spot or wall is detected"""
    check_i = current_i + di
    check_j = current_j + dj
    char_in_front = grid[check_i][check_j]
    
    if char_in_front == ".":
        return spots_in_front
        
    if char_in_front == "#":
        spots_in_front.append((char_in_front, check_i, check_j))
        return spots_in_front
        
    if char_in_front == "O":
        spots_in_front.append((char_in_front, check_i, check_j))
        detect_in_front(grid, spots_in_front, check_i, check_j, di, dj)

grid, steps = [l.splitlines() for l in open("input.txt").read().split("\n\n")]
grid = [list(l) for l in grid]
steps = "".join(steps)
N,M = len(grid), len(grid[0])

ci, cj = get_positions_of_char(grid, char = "@")[0]
for iiidx, step in enumerate(steps):
    #determine next coords
    di, dj = DIRECTIONS[step]
    ni, nj = ci + di, cj + dj

    #check if movement is possible
    spots_in_front = []
    detect_in_front(grid, spots_in_front, ci, cj, di, dj)

    #spot is free
    if len(spots_in_front) == 0:
        grid[ci][cj] = "."
        ci, cj = ni, nj
        grid[ci][cj] = "@"
        continue

    #one or more boxes detected that are pushable.
    elif spots_in_front[0][0] == "O" and spots_in_front[-1][0] != "#":
        grid[ci][cj] = "."
        grid[ni][nj] = "@"
        ci, cj = ni, nj
        
        mi2, mj2 = spots_in_front[-1][1:]
        mi1, mj1 = mi2 + di, mj2 + dj 
        grid[mi1][mj1] = "O"

    #stand still if boxes cannot be moved or robot is standing in front of wall
    elif spots_in_front[0][0] == "#" or spots_in_front[-1][0] == "#":
        continue

box_positions = get_positions_of_char(grid, "O")
ans = sum([100 * i + j for i, j in box_positions])
print(ans)