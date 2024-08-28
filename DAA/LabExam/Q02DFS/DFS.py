def DFS(graph, visited, vertex):
    visited[vertex] = True
    print(vertex)
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            DFS(graph, visited, neighbor)

V = int(input("\nEnter number of vertices: "))
E = int(input("\nEnter number of edges: "))
graph = [[] for _ in range(V)]
visited = [False] * V

print("\nEnter edges (u v) (space separated): ")
for i in range(E):
    u, v = map(int, input(f"Enter edge {i + 1}: ").split())
    graph[u].append(v)
    graph[v].append(u)  # Remove this line if the graph is directed
start = int(input("\nEnter starting vertex: "))
print("\nDFS: ")
DFS(graph, visited, start)