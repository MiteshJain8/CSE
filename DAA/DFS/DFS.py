def DFS(arr,visited,i,n):
    visited[i] = 1
    print(i)
    for j in range(n):
        if(arr[i][j]==1):
            if(visited[j]==0):
                DFS(arr,visited,j,n)

n = int(input("Enter no of vertices: "))
visited = [0 for i in range(n)]
arr = [[0 for i in range(n)] for j in range(n)]

e = int(input("Enter the no of edges: "))
for i in range(e):
    print("Enter edge (u,v): ")
    u = int(input())
    v = int(input())
    arr[u][v], arr[v][u] = 1, 1

print("Adjacency matrix : ")
for i in range(n):
    print(arr[i])

start = int(input("Enter start ele: "))
print("DFS: ")
DFS(arr,visited,start,n)