import copy
DIRECTIONS = {"^":(-1,0), ">":(0,1), "v":(1,0), "<":(0,-1)}
GRID_OG = list(map(list, open("input.txt").read().splitlines()))

def find_starting_pos():
    for d in "^v<>":
        if d in "".join(map(str, GRID_OG)):
            direction = d
            break

    for i in range(len(GRID_OG)):
        if direction in GRID_OG[i]:
            ipos = i
            break
            
    for j in range(len(GRID_OG[ipos])):
        if direction == GRID_OG[ipos][j]: 
            jpos = j
            break

    return direction, ipos, jpos

def get_next_position(direction, ipos, jpos):
    """retrieve coordinates of position in front of guard"""
    a,b = DIRECTIONS[direction]
    ipos_new, jpos_new = ipos+a, jpos+b
    
    return ipos_new, jpos_new

def change_direction(direction):
    """turn clockwise"""
    direction_idx = list(DIRECTIONS.keys()).index(direction)
    direction_idx_new = (direction_idx+1) % 4
    new_direction = list(DIRECTIONS.keys())[direction_idx_new]
    
    return new_direction

def move(direction, ipos, jpos):
    """step forward if possible, else turn"""
    ipos_check, jpos_check = get_next_position(direction, ipos, jpos)

    #stay inside grid
    if not (-1 < ipos_check < len(GRID) and -1 < jpos_check < len(GRID[0])):
        raise IndexError
    
    #if standing in front of a wall, change direction, stand still
    if GRID[ipos_check][jpos_check] == "#":
        new_direction = change_direction(direction)
        ipos_new, jpos_new = ipos, jpos
        
    #if there is no wall, guard moves forward
    else:
        new_direction = direction
        ipos_new, jpos_new = ipos_check, jpos_check
        
    return new_direction, ipos_new, jpos_new

def check_if_loops(direction, ipos, jpos):
    seen = set()
    while True:
        try:
            seen.add((direction, ipos, jpos))
            direction, ipos, jpos = move(direction, ipos, jpos)
            
            if (direction, ipos, jpos) in seen:
                return 1
        except IndexError: #exited the area
            return 0

direction_start, ipos_start, jpos_start = find_starting_pos()

ans = 0
for r in range(len(GRID_OG)):
    for c in range(len(GRID_OG[0])):
        #brute-force check all
        #would be more efficient if ony check the ones in path
        GRID = copy.deepcopy(GRID_OG)
        GRID[r][c] = "#"

        ans += check_if_loops(direction_start, ipos_start, jpos_start)
print(ans)
