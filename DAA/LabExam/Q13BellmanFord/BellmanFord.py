def BellmanFord(graph, src, V):
    dist = [float('inf')] * V
    dist[src] = 0
    for i in range(V-1):
        for edge in graph:
            if (dist[edge[1]] > dist[edge[0]] + edge[2]):
                dist[edge[1]] = dist[edge[0]] + edge[2]
    for edge in graph:
        if (dist[edge[1]] > dist[edge[0]] + edge[2]):
            print("Negative cycle detected")
            return
    print("\nVertex\tDistance from source")
    for i in range(V):
        print(i,"\t",dist[i])

V = int(input("\nEnter number of Vertices: "))
E = int(input("\nEnter number of directed edges: "))
graph = []

print("\nEnter edges [u, v, weight] (space separated):")
for i in range(E):
    graph.append(tuple(map(int,input(f"Edge {i+1}: ").split())))

src = int(input("\nEnter source vertex: "))
BellmanFord(graph, src, V)