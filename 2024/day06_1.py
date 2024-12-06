DIRECTIONS = {"^":(-1,0), ">":(0,1), "v":(1,0), "<":(0,-1)}
GRID = list(map(list, open("input.txt").read().splitlines()))

def find_starting_pos():
    for d in "^v<>":
        if d in "".join(map(str, GRID)):
            direction = d
            break

    for i in range(len(GRID)):
        if direction in GRID[i]:
            ipos = i
            break
            
    for j in range(len(GRID[ipos])):
        if direction == GRID[ipos][j]: 
            jpos = j
            break

    return direction, ipos, jpos

def move(direction, ipos, jpos):
    a,b = DIRECTIONS[direction]
    ipos_new, jpos_new = ipos+a, jpos+b

    if not (-1 < ipos_new < len(GRID) and -1 < jpos_new < len(GRID[0])):
        raise IndexError

    if GRID[ipos_new][jpos_new] == "#":
        direction_idx = list(DIRECTIONS.keys()).index(direction)
        direction_idx_new = (direction_idx+1) % 4
        new_direction = list(DIRECTIONS.keys())[direction_idx_new]
        ipos_new, jpos_new = ipos, jpos
    else:
        new_direction = direction

    return new_direction, ipos_new, jpos_new

direction, ipos, jpos = find_starting_pos()
GRID[ipos][jpos] = "X"

while True:
    try:
        direction, ipos, jpos = move(direction, ipos, jpos)
        GRID[ipos][jpos] = "X"
    except IndexError:
        break
    
ans = sum(row.count("X") for row in GRID)
print(ans)