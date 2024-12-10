def find_reachable_ends(start_pos):
    q = [(0, start_pos)]
    reachable_end_pos = set()

    while q:
        h, pos = q.pop(0)
        i, j = pos

        #check if end has been reached
        if h == 9:
            reachable_end_pos.add((i, j))
            continue

        #move to next accessible steps
        n_coords = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for ni, nj in n_coords:
            if 0 <= ni < N and 0 <= nj < M: 
                nh = h + 1

                if GRID[ni][nj] == nh: #next step
                    q.append((nh, (ni, nj)))

    return reachable_end_pos

GRID = open("input.txt").read().strip().splitlines()
GRID = [[int(x) for x in r] for r in GRID]
N, M = len(GRID), len(GRID[0])

all_start_pos = [(i,j) for j in range(M) for i in range(N) if GRID[i][j] == 0]

ans = 0
for start_pos in all_start_pos:
    reachable_end_pos = find_reachable_ends(start_pos)
    ans += len(reachable_end_pos)
print(ans)
