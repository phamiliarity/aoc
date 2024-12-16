from copy import deepcopy

DIRECTIONS = {"^":(-1,0), ">":(0,1), "v":(1,0), "<":(0,-1)}
DIRECTIONS2 = {v:k for k,v in DIRECTIONS.items()} #{(-1, 0): '^', (0, 1): '>', (1, 0): 'v', (0, -1): '<'}

#helper functions
def get_adjacent_coords(curr_pos):
    i, j = curr_pos
    adj_coords = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    return adj_coords

def get_new_dir(curr_pos, next_pos):
    global DIRECTIONS2

    ci, cj = curr_pos
    ni, nj = next_pos

    ndi, ndj = ni - ci, nj - cj
    return DIRECTIONS2[(ndi,ndj)]

def get_number_of_turns(curr_dir, new_dir):
    global DIRECTIONS

    curr_dir_idx = list(DIRECTIONS.keys()).index(curr_dir)
    new_dir_idx = list(DIRECTIONS.keys()).index(new_dir)
    return abs(curr_dir_idx - new_dir_idx) % 2

#wrappers (sub)
def get_movement_info(curr_pos, next_pos):
    global TURN_COST, STEP_COST

    new_dir = get_new_dir(curr_pos, next_pos)
    n_turns = get_number_of_turns(curr_dir, new_dir)
    cost = n_turns * TURN_COST + STEP_COST

    #print(f"\t{next_pos}\t\t{new_dir}\t\t{cost}")
    return new_dir, cost

def find_next_possible_steps(curr_pos):
    global WALL_POS

    possible_steps = []

    #get adjacent positions
    next_poss = [_ for _ in get_adjacent_coords(curr_pos) if _ not in WALL_POS]
    for next_pos in next_poss:
        new_dir, new_cost = get_movement_info(curr_pos, next_pos)  
        possible_steps.append((next_pos, new_dir, new_cost))

    return possible_steps #[(step, direction, cost), ...]

#wrappers (main)
def get_best_step(curr_pos, curr_dir, curr_total_cost, visited):
    """A* algo to determine the movement with lowest cost"""
    global TO_PROCESS, END_POS

    possible_steps = find_next_possible_steps(curr_pos)

    #determine best step from the list
    steps_info = []
    for possible_step, possible_dir, possible_cost in possible_steps:
        new_total_cost = curr_total_cost + possible_cost
        stored_info = visited.get(possible_step, [float("inf")])
        stored_total_cost = stored_info[0]

        #skip checking this step if it has already been visited in a more efficient route
        if possible_step in visited and possible_step != END_POS and \
            visited[possible_step][0] < new_total_cost:
            continue

        #don't backtrack
        check_dir = get_new_dir(curr_pos, possible_step)
        opposite_dir = {"<": ">", ">":"<", "v":"^", "^":"v"}[curr_dir]
        if opposite_dir == check_dir:
            continue

        #stored path is more efficient
        if stored_total_cost < new_total_cost:
            possible_total_cost = stored_total_cost
            possible_dir = stored_info[2]

        #detected path is more efficient
        else:
            visited[possible_step] = (new_total_cost, curr_pos, possible_dir)
            possible_total_cost = new_total_cost

        steps_info.append((possible_step, possible_dir, possible_total_cost))

    if len(steps_info) == 0:
        return None

    steps_info.sort(key=lambda x:x[2])
    best_step = steps_info[0]

    TO_PROCESS += steps_info[1:]

    return best_step

def get_positions_of_char(grid, char):
    """get coords of a character in a grid"""
    global N,M
    pos = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == char:
                pos.append((i,j))
    return pos

#input
grid = open("input.txt").read()
grid = [list(l) for l in grid.splitlines()]
N,M = len(grid), len(grid[0])

#constants
STEP_COST = 1
TURN_COST = 1000
WALL_POS = tuple(get_positions_of_char(grid, "#"))

#initialise
START_POS, start_dir = get_positions_of_char(grid, "S")[0], ">"
END_POS = get_positions_of_char(grid, "E")[0]

#process
TO_PROCESS = []
curr_pos, curr_dir, curr_total_cost = START_POS, start_dir, 0
visited = dict() # {(pi, pj) : (cost_from_start, parent, direction)...}
reached_ends_from = [] #[(parent, cost), ...]

while True:
    ci, cj = curr_pos

    best_step = get_best_step(curr_pos, curr_dir, curr_total_cost, visited)

    if best_step == None: #hit a dead end, go back to the next possible option
        if len(TO_PROCESS) == 0:
            break #all tiles inspected
        curr_pos, curr_dir, curr_total_cost = TO_PROCESS.pop(0)
        continue

    parent_pos = curr_pos
    curr_pos, curr_dir, curr_total_cost = best_step
    
    if curr_pos == END_POS:
        reached_ends_from.append((parent_pos, curr_total_cost))
        if len(TO_PROCESS) > 0:
            curr_pos, curr_dir, curr_total_cost = TO_PROCESS.pop(0)
            continue

reached_ends_from.sort(key=lambda x:x[1])
best_score = reached_ends_from[0][1]
print("\n", best_score)