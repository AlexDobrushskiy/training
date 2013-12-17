# G = {'a': {'b':{100:[...], 101:[...], ...}}}

# G = {'a': {'b':1, 'c':2, 'd':3}, ...}

def dijkstra(G, v):
	"""
	Dijkstra with path for every node
	"""
     # init section
     # ---------------------------------------
     cost = {}
     for node in G:
          cost[node] = float('inf')
     cost[v] = 0
     to_visit = [(v, 0)]
     visited = []
     paths = {v: [v]}
     # ---------------------------------------
     while to_visit:
          node, dist = to_visit.pop()
          for i in G[node]:
               if (dist + G[node][i]) < cost[i]:
                    cost[i] = dist + G[node][i]
                    paths[i] = paths[node] + [i]
               for j in to_visit:
                    if j[0] == i:
                         to_visit.remove((j[0], j[1]))
               if i not in visited:
                    to_visit.append((i, cost[i]))
                    to_visit.sort(key=lambda x: x[1])
          visited.append(node)
     return cost, paths


G = {'a':{'b':1, 'c':1}, 'b':{'c':5, 'd':2}, 'c':{'a':2, 'b':1, 'd':1}, 'd':{'a':3}}	
cost, paths =  dijkstra(G, 'a')

print cost
print paths