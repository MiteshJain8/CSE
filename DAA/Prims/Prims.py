INF = 999

def Prims(G, visited, V): 
    edges, cost = 0, 0
    visited[0] = True
    print("Edge: Weight")
    while (edges < V-1):
        minimum, x, y = INF, 0, 0
        for i in range(V):
            if visited[i]:
                for j in range(V):
                    if ((not visited[j]) and G[i][j]):
                        if minimum > G[i][j]:
                            minimum, x, y = G[i][j], i, j
        print(str(x) + " " + str(y) + ":" + str(G[x][y]))
        visited[y] = True
        cost += G[x][y]
        edges += 1
    print("Cost of minimum spanning tree:", cost)

n = int(input("\nEnter no of vertices: "))
visited = [0 for i in range(n)]

arr = [[999 for i in range(n)] for j in range(n)] 
for i in range(n):
    arr[i][i] = 0

print("\nInitially adj mat:")
for i in range(n):
    print(arr[i])

e = int(input("Enter the no of edges: "))
for i in range(e):
    print("Enter edge (u,v): ")
    u = int(input())
    v = int(input())
    weight = int(input("Enter its weight: "))
    arr[u][v], arr[v][u] = weight, weight

print("\nAdjacency matrix : ")
for i in range(n):
    print(arr[i])

print("\nPrims: ")
Prims(arr, visited,n)