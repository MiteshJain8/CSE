def DFS(Graph,visited,i,V):
    visited[i] = 1
    print(i)
    for j in range(V):
        if(Graph[i][j]==1):
            if(visited[j]==0):
                DFS(Graph,visited,j,V)

V = int(input("\nEnter no of vertices: "))
visited = [0 for i in range(V)]
Graph = [[0 for i in range(V)] for j in range(V)]

E = int(input("\nEnter the no of edges: "))
for i in range(E):
    print(f"Enter edge {i+1} separated by spaces: ")
    u, v = map(int, input().split())
    Graph[u][v], Graph[v][u] = 1, 1

print("\nAdjacency matrix : ")
for i in range(V):
    print(Graph[i])

start = int(input("\nEnter start ele: "))
print("\nDFS: ")
DFS(Graph,visited,start,V)