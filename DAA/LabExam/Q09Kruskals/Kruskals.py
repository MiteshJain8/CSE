def find(parent, i): 
    if parent[i] != i: 
        parent[i] = find(parent, parent[i]) 
    return parent[i]

def Kruskals(graph, V):
    mst = []
    graph = sorted(graph, key=lambda item: item[2])
    parent = [i for i in range(V)]
    cost, edges, i = 0, 0, 0
    while edges < V-1:
        u, v, weight = graph[i]
        i+=1
        x, y = find(parent, u), find(parent, v)
        if x != y:
            edges += 1
            mst.append([u, v, weight])
            parent[y] = parent[x]
            cost += weight
    print("\nMinimum Spanning Tree: ", mst)
    print("\nMinimum Spanning Tree Cost: ", cost)

V = int(input("\nEnter no of vertices: "))
graph = []
E = int(input("\nEnter the no of edges: "))
print("Enter edges and their weight separated by space(u v weight)")
for i in range(E):
    u, v, weight = map(int, input(f"Edge {i+1}: ").split())
    graph.append([u, v, weight])
Kruskals(graph, V)