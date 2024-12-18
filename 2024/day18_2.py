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

#INIT
N = M = 71

#initialise graph object where orthogonal nodes are connected
grid_positions = [(i,j) for j in range(M) for i in range(N)]
grid = Graph()
for pos in grid_positions:
    adjs = get_adj(pos)
    for adj in adjs:
        grid.add_edge(pos, adj)

#initialise the shortest path
start, end = (0,0), (N-1,M-1)
shortest_path = grid.shortest_path(start, end)

#load bytes
b = [tuple(map(int, l.strip().split(","))) for l in open("input.txt").readlines()]

try:
    for bb in b:
        #byte falls: delete connection
        for parent in grid.graph[bb]:
            grid.graph[parent].remove(bb)
        grid.graph.pop(bb)

        #recalculate path if byte blocks the current optimal path
        if bb in shortest_path:
            shortest_path = grid.shortest_path(start, end)
except IndexError:
    print(",".join(map(str, bb)))
