import re

DIRECTIONS = {"^":(-1,0), ">":(0,1), "v":(1,0), "<":(0,-1)}

def get_positions_of_char(grid, char):
    """get coords of a character in a grid"""
    pos = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == char:
                pos.append((i,j))
    return pos

def detect_in_front(grid, seen, spots_in_front, current_i, current_j, di, dj):
    """get elements in front of robot until a free spot or wall is detected"""
    check_i = current_i + di
    check_j = current_j + dj
    char_in_front = grid[check_i][check_j]
    
    if char_in_front == ".":
        return spots_in_front
        
    if char_in_front == "#":
        spots_in_front.append((char_in_front, check_i, check_j))
        return spots_in_front
        
    if char_in_front in "[]":
        if char_in_front == "[":
            spots = [(check_i, check_j), (check_i, check_j+1)]
        if char_in_front == "]":
            spots = [(check_i, check_j), (check_i, check_j-1)]
            
        for si, sj in spots:
            if (si, sj) in seen: continue
            seen.add((si, sj))
            spots_in_front.append((grid[si][sj], si, sj))
            detect_in_front(grid, seen, spots_in_front, si, sj, di, dj)

grid, steps = open("input.txt").read().split("\n\n")
grid = list(map(list, (grid.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.").splitlines())))
steps = steps.replace("\n", "")
N,M = len(grid), len(grid[0])


ci, cj = get_positions_of_char(grid, char = "@")[0]

for iiidx, step in enumerate(steps):
    #determine next coords
    di, dj = DIRECTIONS[step]
    ni, nj = ci + di, cj + dj

    #check if movement is possible
    spots_in_front = []
    seen = set()
    detect_in_front(grid, seen, spots_in_front, ci, cj, di, dj)

    #spot is free
    if len(spots_in_front) == 0:
        grid[ci][cj] = "."
        ci, cj = ni, nj
        grid[ci][cj] = "@"
        continue
        
    #stand still if boxes cannot be moved or robot is standing in front of wall
    elif "#" in [char for char, _, _ in spots_in_front]:
        continue
        
    #one or more boxes detected that are pushable.
    else:
        updated = set()
        for char, bi, bj in spots_in_front:
            #remove the side parts artifacts
            if di in [1, -1]:
                if char == "[" and grid[bi][bj+1] == "]" and (bi,bj+1) not in updated:
                    grid[bi][bj+1] = "."
                elif char == "]" and grid[bi][bj-1] == "[" and (bi,bj-1) not in updated:
                    grid[bi][bj-1] = "."
            nbi, nbj = bi + di, bj + dj
            grid[nbi][nbj] = char
            updated.add((nbi, nbj))

        grid[ci][cj] = "."
        ci, cj = ni, nj
        grid[ci][cj] = "@"

box_positions = get_positions_of_char(grid, "[")
ans = sum([100 * i + j for i, j in box_positions])
print(ans)