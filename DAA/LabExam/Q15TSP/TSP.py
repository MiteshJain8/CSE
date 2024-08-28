def tsp(graph, visited, curr_pos, V, count, cost, path):
    if count == V and graph[curr_pos][path[0]]:
        return cost + graph[curr_pos][path[0]], path + [path[0]]
    ans = float('inf')
    best_path = []
    for i in range(V):
        if not visited[i] and graph[curr_pos][i] < float('inf'):
            visited[i] = True
            new_cost, new_path = tsp(graph, visited, i, V, count + 1, cost + graph[curr_pos][i], path + [i])
            if new_cost < ans:
                ans = new_cost
                best_path = new_path
            visited[i] = False
    return ans, best_path

V = int(input("\nEnter no of vertices: "))
visited = [False for _ in range(V)]

Graph = [[float('inf')] * V for _ in range(V)] 
for i in range(V):
    Graph[i][i] = 0

E = int(input("Enter the no of edges: "))
print("Enter edges and their weight separated by space(u v weight)")
for i in range(E):
    u, v, weight = map(int, input(f"Edge {i+1}: ").split())
    Graph[u][v] = weight
    Graph[v][u] = weight

src = int(input("Enter the source node: "))
visited[src] = True

min_cost, tour_path = tsp(Graph, visited, src, V, 1, 0, [src])
print("Minimum Cost of Tour:", min_cost)
print("Path Taken:", " -> ".join(map(str, tour_path)))