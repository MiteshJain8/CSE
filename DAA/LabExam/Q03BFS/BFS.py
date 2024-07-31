def BFS(arr,visited,i,V):
    queue = []
    visited[i] = 1
    print(i)
    queue.append(i)
    while queue:
        vertex = queue.pop(0)
        for j in range(V):
            if(arr[vertex][j]==1):
                if(visited[j]==0):
                    visited[j]=1
                    print(j)
                    queue.append(j)

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
print("\nBFS: ")
BFS(Graph,visited,start,V)