def get_adj(pos):
    i, j = pos
    adj = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    return [(ni, nj) for ni, nj in adj if 0 <= ni < N and 0 <= nj < M]

class Graph():
    def __init__(self, graph = {}):
        self.graph = graph

    def add_edge(self, parent, child):
        if parent not in self.graph:
            self.graph[parent] = set()
        self.graph[parent].add(child)

    def determine_shortest_paths(self, start = (0,0)):
        """bfs"""

        #init distance to start
        distances = {child: float("inf") for child in self.graph}
        distances[start] = 0

        #create queue
        q = []
        q.append(start)

        #travel through grid
        visited = set()
        while q:
            curr_node = q.pop(0)
            curr_distance = distances[curr_node]

            if curr_node in visited: continue
            visited.add(curr_node)

            for child in self.graph[curr_node]:
                new_distance = curr_distance + 1
                if new_distance <= distances[child]:
                    distances[child] = new_distance
                    q.append(child)
        return distances

#load input
txt = [list(l) for l in open("input.txt").read().splitlines()]
N,M = len(txt), len(txt[0])

#get positions, exclude outerwalls
open_positions, wall_positions = [], []
for i in range(1,N-1):
    for j in range(1,M-1):
        if txt[i][j] == "S":
            start_pos = (i,j)
        elif txt[i][j] == "E":
            end_pos = (i,j)

        if txt[i][j] == "#":
            wall_positions.append((i,j))
        else:
            open_positions.append((i,j))

#initialise grid with connected open positions
grid = Graph()
for pos in open_positions:
    adjs = get_adj(pos)
    for adj in adjs:
        if adj in open_positions:
            grid.add_edge(pos, adj)

#initialise original shortest path
distances_from_start = grid.determine_shortest_paths(start_pos)
distances_from_end = grid.determine_shortest_paths(end_pos)
original_time = distances_from_start[end_pos]

#check how much time is saved for cheats within range
max_dist = 20
min_abs_dt = 100

ans = 0
for spos, st in distances_from_start.items():
    sx, sy = spos
    for epos, et in distances_from_end.items():
        ex, ey = epos

        #dist between the positions should be eq/less than max cheat dist
        pos_dist = abs(ex-sx) + abs(ey-sy)
        if pos_dist > max_dist: continue
        
        #saved time should be >= minimum required time saved
        new_time = distances_from_start[spos] + pos_dist + distances_from_end[epos]
        if original_time - new_time >= min_abs_dt:
            ans += 1
print(ans)