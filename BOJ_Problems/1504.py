def dijkstraWithWayPoints(start, end, waypoints = None):
    if waypoints: return dijkstraWithWayPoints(start, waypoints[0]) + dijkstraWithWayPoints(waypoints[0], waypoints[1]) + dijkstraWithWayPoints(waypoints[1], end)
    else:
        minimun_distances = [None] + [INF] * n
        visited = [None] + [False] * n
        minimun_distances[start] = 0

        while visited[end] != True and False in visited:
            closest_node, closest_distance = None, INF
            for node_idx in range(1, n+1):
                if not visited[node_idx]:
                    if minimun_distances[node_idx] < closest_distance:
                        closest_node = node_idx
                        closest_distance = minimun_distances[node_idx]

            for node, dist in connections[closest_node]:
                minimun_distances[node] = min(minimun_distances[node], minimun_distances[closest_node] + dist)
            visited[closest_node] = True
        
        return minimun_distances[end]

INF = int(1e6)
n, e = map(int, input().split())
connections = {i+1: [] for i in range(n)}
for _ in range(e):
    node1, node2, distance = map(int, input().split())
    connections[node1].append((node2, distance))
    connections[node2].append((node1, distance))
v1, v2 = map(int, input().split())

try:
    result1 = dijkstraWithWayPoints(start = 1, end = n, waypoints = [v1, v2])
    result2 = dijkstraWithWayPoints(start = 1, end = n, waypoints = [v2, v1])
    print(min(result1, result2))
except: print(-1)