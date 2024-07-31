def Prims(Graph, visited, V): 
    edges, cost = 0, 0
    visited[0] = True
    print("Edge: Weight")
    while (edges < V-1):
        minimum, x, y = float('inf'), 0, 0
        for i in range(V):
            if visited[i]:
                for j in range(V):
                    if ((not visited[j]) and Graph[i][j]):
                        if minimum > Graph[i][j]:
                            minimum, x, y = Graph[i][j], i, j
        print(str(x) + " " + str(y) + ":" + str(Graph[x][y]))
        visited[y] = True
        cost += Graph[x][y]
        edges += 1
    print("Cost of minimum spanning tree:", cost)

V = int(input("\nEnter no of vertices: "))
visited = [False for i in range(V)]

Graph = [[float('inf') for i in range(V)] for j in range(V)] 
for i in range(V):
    Graph[i][i] = 0

E = int(input("Enter the no of edges: "))
print("Enter edges and their weight separated by space(u v weight)")
for i in range(E):
    print(f"Edge {i+1}: ")
    u, v, weight = map(int, input().split())
    Graph[u][v], Graph[v][u] = weight, weight

print("\nAdjacency matrix : ")
for i in range(V):
    print(Graph[i])

print("\nPrims: ")
Prims(Graph, visited,V)