def DFS(arr,visited,i,n):
    visited[i] = 1
    print(i)
    for j in range(n):
        if(arr[i][j]==1):
            if(visited[j]==0):
                DFS(arr,visited,j,n)


n = int(input("Enter no of vertices: "))
visited = [0 for i in range(n)]
e = int(input("Enter the no of edges: "))
arr = [[0 for i in range(n)] for j in range(n)]
for i in range(e):
    print("Enter edge (u,v): ")
    vi = int(input())
    vj = int(input())
    arr[vi][vj] = 1
    arr[vj][vi] = 1
print("Adjacency matrix : ",arr)
strt = int(input("Enter start ele: "))
print("DFS: ")
DFS(arr,visited,strt,n)