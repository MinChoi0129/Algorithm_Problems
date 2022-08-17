import heapq, sys
input = lambda : sys.stdin.readline().rstrip()
number_of_nodes, number_of_edges, start_node, Q, INF = *map(int, input().split()), int(input()), [], 1e9
node_connections, node_distances = [ [] * (number_of_nodes+1) for _ in range(number_of_nodes+1) ], [INF] * (number_of_nodes+1)

for _ in range(number_of_edges):
    node1, node2, distance = map(int, input().split())
    node_connections[node1].append([node2, distance])

heapq.heappush(Q, [0, start_node])
node_distances[start_node] = 0
while Q:
    shortest_distance, present_node = heapq.heappop(Q)
    if not shortest_distance < node_distances[present_node]:
        for connection in node_connections[present_node]:
            new_distance = shortest_distance + connection[1]
            if new_distance < node_distances[connection[0]]: node_distances[connection[0]] = new_distance; heapq.heappush(Q, [new_distance, connection[0]])

for i in range(1, number_of_nodes+1): print("INF" if node_distances[i] == INF else node_distances[i])