def count_paths_to_end(start_pos):
    q = [(0, start_pos)]
    n_end_reached = 0

    while q:
        h, pos = q.pop(0)
        i, j = pos

        #check if end has been reached
        if h == 9:
            n_end_reached += 1
            continue

        #move to next accessible steps
        n_coords = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for ni, nj in n_coords:
            if 0 <= ni < N and 0 <= nj < M: 
                nh = h + 1

                if GRID[ni][nj] == nh: #next step
                    q.append((nh, (ni, nj)))

    return n_end_reached

GRID = open("input.txt").read().strip().splitlines()
GRID = [[int(x) for x in r] for r in GRID]
N, M = len(GRID), len(GRID[0])

all_start_pos = [(i,j) for j in range(M) for i in range(N) if GRID[i][j] == 0]

ans = 0
for start_pos in all_start_pos:
    n_end_reached = count_paths_to_end(start_pos)
    ans += n_end_reached
print(ans)
