def DFS(graph, visited, vertex):
    visited[vertex] = True
    print(vertex)
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            DFS(graph, visited, neighbor)

V = int(input("\nEnter number of vertices: "))
graph = [[] for _ in range(V)]
visited = [False] * V

E = int(input("\nEnter number of edges: "))
for i in range(E):
    print(f"Enter edge {i + 1} separated by spaces: ")
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # Remove this line if the graph is directed

print("\nAdjacency list: ")
for i in range(V):
    print(f"{i}: {graph[i]}")

start = int(input("\nEnter starting vertex: "))
print("\nDFS: ")
DFS(graph, visited, start)