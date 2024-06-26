import heapq

INF = 999

def Dijkstras(graph, src, n):
    shortest_path = [INF] * n
    shortest_path[src] = 0
    priority_queue = [(0, src)]  # (distance, vertex)

    while priority_queue:
        current_distance, u = heapq.heappop(priority_queue)

        if current_distance > shortest_path[u]:
            continue

        for neighbor, weight in graph[u]:
            distance = current_distance + weight

            if distance < shortest_path[neighbor]:
                shortest_path[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    for i in range(n):
        print(f"{i}: {shortest_path[i]}")

n = int(input("\nEnter number of vertices: "))
graph = [[] for _ in range(n)]
e = int(input("Enter the number of edges: "))
for i in range(e):
    print("Enter edge (u, v): ")
    u = int(input())
    v = int(input())
    weight = int(input("Enter its weight: "))
    graph[u].append((v, weight))
    graph[v].append((u, weight))

print("\nAdjacency list: ")
for i in range(n):
    print(f"{i}: {graph[i]}")

src = int(input("\nEnter source vertex: "))
print("\nShortest path:")
Dijkstras(graph, src, n)