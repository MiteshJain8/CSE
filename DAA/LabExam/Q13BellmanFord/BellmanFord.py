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
print("\nEnter adjacency list edges [u, v, weight] separated by space:")
for i in range(E):
    graph.append(list(map(int,input(f"Edge {i+1}: ").split())))
src = int(input("\nEnter source vertex: "))
print("\nGraph:",graph)
BellmanFord(graph, src, V)