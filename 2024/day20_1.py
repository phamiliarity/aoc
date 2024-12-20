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

    def del_edge(self, parent, child):
        self.graph[parent].remove(child)
        if not self.graph[parent]: del self.graph[parent]

    def determine_shortest_paths(self, start = (0,0)):
        """bfs"""

        #init distance to start
        distances = {child: float("inf") for child in self.graph}
        distances[start] = 0

        parents = {node: set() for node in self.graph}

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
                    parents[child].add(curr_node)

                    q.append(child)
        return distances, parents

    def shortest_path(self, start, end):
        distances, parents = self.determine_shortest_paths(start)
        path = []
        curr_node = end
        visited = set()

        while curr_node != start:
            path.append(curr_node)
            visited.add(curr_node)

            pparents = parents.get(curr_node, [])
            curr_node = [node for node in pparents if node not in visited][0]

        path.reverse()

        return path

def get_positions_of_char(grid, char):
    """get coords of a character in a grid"""
    global N,M
    pos = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == char:
                pos.append((i,j))
    return pos

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
original_shortest_path = grid.shortest_path(start_pos, end_pos)
original_time = len(original_shortest_path)

#get wall positions which could create shortcuts:
#i.e. walls touching >=2 open positions
possible_walls = {}
for wall_position in wall_positions:
    adjs = get_adj(wall_position)
    adj_opens = [adj for adj in adjs if adj in open_positions]
    if len(adj_opens) >= 2:
        possible_walls[wall_position] = adj_opens

#analyse effect of disabling wall
min_dt = -100
ans = 0
for possible_wall, new_opens in possible_walls.items():
    #add new connections
    for new_open in new_opens:
        grid.add_edge(possible_wall, new_open)
        grid.add_edge(new_open, possible_wall)

    #calculate time difference
    new_shortest_path = grid.shortest_path(start_pos, end_pos)
    new_time = len(new_shortest_path)
    dt = new_time - original_time
    if dt <= min_dt:
        ans += 1

    #delete connections
    for new_open in new_opens:
        grid.del_edge(possible_wall, new_open)
        grid.del_edge(new_open, possible_wall)
print(ans)