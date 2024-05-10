def BFS(arr,visited,i,n):
    queue = []
    visited[i] = 1
    print(i)
    queue.append(i)
    while(len(queue)!=0):
        vertex = queue.pop(0)
        for j in range(n):
            if(arr[vertex][j]==1):
                if(visited[j]==0):
                    visited[j]=1
                    print(j)
                    queue.append(j)

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
print("BFS: ")
BFS(arr,visited,strt,n)