def Prims(Graph, visited, src, V): 
    edges, cost = 0, 0
    visited[src] = True
    print("Edge: Weight")
    while edges < V-1:
        minimum, x, y = float('inf'), 0, 0
        for i in range(V):
            if visited[i]:
                for j in range(V):
                    if not visited[j] and Graph[i][j] < float('inf'):
                        if Graph[i][j] < minimum:
                            minimum, x, y = Graph[i][j], i, j
        print(f"{x} - {y}: {minimum}")
        visited[y] = True
        cost += minimum
        edges += 1
    print("Cost of minimum spanning tree:", cost)

V = int(input("\nEnter no of vertices: "))
visited = [False for i in range(V)]

Graph = [[float('inf') for i in range(V)] for j in range(V)] 
for i in range(V):
    Graph[i][i] = 0

E = int(input("Enter the no of edges: "))
print("Enter edges and their weight (space separated) (u v weight)")
for i in range(E):
    u, v, weight = map(int, input(f"Edge {i+1}: ").split())
    Graph[u][v] = weight
    Graph[v][u] = weight

src = int(input("\nEnter the source vertex: "))
print("\nPrims: ")
Prims(Graph, visited, src, V)