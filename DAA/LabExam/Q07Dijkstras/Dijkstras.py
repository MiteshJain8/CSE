def Dijkstras(graph, src, V):
    shortest_path = [float('inf')] * V
    shortest_path[src] = 0
    queue = [(0, src)]  # (distance, vertex)
    predecessor = [-1] * V  # To store the path

    while queue:
        current_distance, u = queue.pop(0)

        if current_distance > shortest_path[u]:
            continue

        for neighbor, weight in graph[u]:
            distance = current_distance + weight

            if distance < shortest_path[neighbor]:
                shortest_path[neighbor] = distance
                predecessor[neighbor] = u
                queue.append((distance, neighbor))

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
graph = [[] for i in range(V)]
E = int(input("Enter the number of edges: "))
for i in range(E):
    print("Enter edge (u, v): ")
    u = int(input())
    v = int(input())
    weight = int(input("Enter its weight: "))
    graph[u].append((v, weight))
    graph[v].append((u, weight))

print("\nAdjacency list: ")
for i in range(V):
    print(f"{i}: {graph[i]}")

src = int(input("\nEnter source vertex: "))
Dijkstras(graph, src, V)