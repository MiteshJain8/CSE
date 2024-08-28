def Dijkstras(graph, src, V):
    shortest_path = [float('inf')] * V
    shortest_path[src] = 0
    queue = set([src])  # Set of vertices to be processed
    predecessor = [-1] * V  # To store the path

    while queue:
        # Find the vertex with the minimum distance
        u = min(queue, key=lambda vertex: shortest_path[vertex])
        queue.remove(u)

        for neighbor, weight in graph[u]:
            distance = shortest_path[u] + weight

            if distance < shortest_path[neighbor]:
                shortest_path[neighbor] = distance
                predecessor[neighbor] = u
                queue.add(neighbor)

    print("\nVertex\tDistance from source\tPath")
    for i in range(V):
        if shortest_path[i] == float('inf'):
            print(f"{i}\t\t{shortest_path[i]}\t\tNo path")
        else:
            path = []
            crawl = i
            while crawl != -1:
                path.append(crawl)
                crawl = predecessor[crawl]
            path.reverse()
            print(f"{i}\t\t{shortest_path[i]}\t\t{' -> '.join(map(str, path))}")

V = int(input("\nEnter number of vertices: "))
E = int(input("Enter the number of edges: "))

graph = [[] for i in range(V)]
print("Enter edges and their weight (space separated) (u v weight)")
for i in range(E):
    print(f"Edge {i+1}: ")
    u, v, weight = map(int, input().split())
    graph[u].append((v, weight))
    graph[v].append((u, weight)) # Remove this line for directed graph

src = int(input("\nEnter source vertex: "))
Dijkstras(graph, src, V)