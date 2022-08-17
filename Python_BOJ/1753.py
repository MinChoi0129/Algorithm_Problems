v, e, k, INF = *map(int, input().split()), int(input()), 1e9
node_connections, distance = [ [] * (v+1) for _ in range(1, v+1) ], [INF] * (v+1)

for _ in range(e):
    node1, node2, distance = map(int, input().split())
    node_connections[node1].append([node2, distance])

for i in range(1, v+1):
    print("INF" if distance[i] == INF else distance[i])