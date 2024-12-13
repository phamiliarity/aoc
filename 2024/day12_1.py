def get_valid_adjacent_coords(curr_pos):
    i, j = curr_pos
    adj_coords = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    adj_coords = [(ni, nj) for ni, nj in adj_coords if 0 <= ni < N and 0 <= nj < M]

    return adj_coords

def get_grouped_plots(seen, curr_pos, curr_label):
    """dfs to get all connected plots of same label"""
    i, j = curr_pos
    seen.append((i,j))

    adj_coords = get_valid_adjacent_coords(curr_pos)
    for ni, nj in adj_coords:
        if (ni, nj) not in seen and GRID[ni][nj] == curr_label:
            get_grouped_plots(seen, (ni,nj), curr_label)

def calculate_perimeter(group):
    """count how often an edge is adjacent to a tile with a different label"""
    curr_label = GRID[group[0][0]][group[0][1]]

    perimeter = 0
    for i, j in group:
        adj_coords = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for ni, nj in adj_coords:
            if 0 <= ni < N and 0 <= nj < M:
                if GRID[ni][nj] != curr_label:
                    perimeter += 1
            else: #hit the border
                perimeter += 1 

    return perimeter

txt = open("input.txt").read()
GRID = list(map(list, txt.strip().splitlines()))
N, M = len(GRID), len(GRID[0])

ans = 0
grouped = [] #list of visited nodes
for i in range(N):
    for j in range(M):
        if (i,j) not in grouped:

            #get group of adjacent tiles with same label
            grouped_plots = []
            get_grouped_plots(grouped_plots, (i,j), GRID[i][j])
            grouped += grouped_plots

            #calculate fence
            area = len(grouped_plots)
            perimeter = calculate_perimeter(grouped_plots)
            ans += area * perimeter
print(ans)