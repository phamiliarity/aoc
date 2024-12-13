def get_adjacent_coords(curr_pos, in_grid=True):
    i, j = curr_pos
    adj_coords = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    if in_grid:
        adj_coords = [(ni, nj) for ni, nj in adj_coords if 0 <= ni < N and 0 <= nj < M]

    return adj_coords

def get_grouped_plots(seen, curr_pos, curr_label):
    """dfs to get all connected plots of same label"""
    i, j = curr_pos
    seen.append((i,j))

    adj_coords = get_adjacent_coords(curr_pos)
    for ni, nj in adj_coords:
        if (ni, nj) not in seen and GRID[ni][nj] == curr_label:
            get_grouped_plots(seen, (ni,nj), curr_label)

def get_perimeter_coords(group):
    side_dict = {(0,1): "right", (0,-1):"left", (-1,0):"top", (1,0):"bottom"} #to make it readable..

    perimeter_plots = []
    curr_label = GRID[group[0][0]][group[0][1]]

    for i, j in group:
        curr_peri = []
        adj_coords = get_adjacent_coords((i,j), in_grid=False)
        for ni, nj in adj_coords:
            di, dj = ni-i, nj-j
            side = side_dict[(di, dj)]
            if 0 <= ni < N and 0 <= nj < M:
                if GRID[ni][nj] != curr_label: #only if it doesnt belong to the plot
                    curr_peri.append((ni, nj, side))
            else: #hit the border
                curr_peri.append((ni, nj, side))
        perimeter_plots += curr_peri
    return perimeter_plots

def get_segments(checking, seen, curr_pos, side):
    """dfs to get all connected plots of same side"""
    i, j = curr_pos
    seen.append((i,j))

    if side in ["top", "bottom"]:
        adj_coords = [(i, j-1), (i, j+1)]
    else:
        adj_coords = [(i-1, j), (i+1, j)]

    for ni, nj in adj_coords:
        if (ni, nj) not in seen and (ni, nj) in checking:
            get_segments(checking, seen, (ni,nj), side)

def count_fence_segments_by_side(perimeter_plots):
    """count n consecutive fence segments that are on the same side"""
    n_sides = 0

    for side in ["top","left","right","bottom"]:
        checking = [plot[:2] for plot in perimeter_plots if plot[2] == side]
        segments = set()
        seen = []

        #group the fences of the current inspected side
        for check in checking:
            curr_pos = check[:2]
            if check not in seen:
                seen = []
            else:
                continue
            get_segments(checking, seen, curr_pos, side)
            segments.add(tuple(sorted(seen)))

        n_sides += len(segments)
    return n_sides

txt = open("input.txt").read()
GRID = list(map(list, txt.strip().splitlines()))
N, M = len(GRID), len(GRID[0])

ans = 0
grouped = [] #list of visited nodes
for ci in range(N):
    for cj in range(M):
        if (ci, cj) not in grouped:
            #get group of adjacent tiles with same label
            grouped_plots = []
            get_grouped_plots(grouped_plots, (ci,cj), GRID[ci][cj])
            grouped += grouped_plots

            #determine fence
            perimeter_plots = get_perimeter_coords(grouped_plots)
            i, j, side = perimeter_plots[0]

            #calculate fence
            area = len(grouped_plots)
            n_fence_fragments = count_fence_segments_by_side(perimeter_plots)

            ans += area*n_fence_fragments
print(ans)
