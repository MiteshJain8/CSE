def find(parent, i): 
    if parent[i] != i: 
        parent[i] = find(parent, parent[i]) 
    return parent[i]

def union(parent, rank, x, y): 
    if rank[x] < rank[y]: 
        parent[x] = parent[y] 
    elif rank[x] > rank[y]: 
        parent[y] = parent[x] 
    else: 
        parent[y] = parent[x] 
        rank[x] += 1

def Kruskals(graph, V):
    mst = []
    graph = sorted(graph, key=lambda item: item[2])
    parent = [i for i in range(V)]
    rank = [0 for i in range(V)]
    cost, edges, i = 0, 0, 0
    while edges < V-1:
        u, v, weight = graph[i]
        i+=1
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            edges += 1
            mst.append([u, v, weight])
            union(parent, rank, x, y)
            cost += weight
    print("\nParent array after union: ", parent)
    print("\nRank array after union: ", rank)
    print("\nMST: ", mst)
    print("\nMinimum Spanning Tree Cost: ", cost)

n = int(input("\nEnter no of vertices: "))
parent = [i for i in range(n)]
rank = [0 for i in range(n)]
print("\nInitially parent array: ", parent)
print("\nInitially rank array: ", rank)
graph = []
e = int(input("\nEnter the no of edges: "))
for i in range(e):
    print("Enter edge (u,v): ")
    u = int(input())
    v = int(input())
    weight = int(input("Enter its weight: "))
    graph.append([u, v, weight])

Kruskals(graph, n)