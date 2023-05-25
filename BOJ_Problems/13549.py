import heapq

INF, MAX_SIZE = int(1e9), int(1e5)
n, k = map(int, input().split())

distances = {num: INF for num in range(MAX_SIZE+1)}
distances[n] = 0

Q = [(0, n)]

while Q:
    dist, node = heapq.heappop(Q)
    for new_dist, new_node in [(0, 2 * node), (1, node + 1), (1, node - 1)]:
        if 0 <= new_node <= MAX_SIZE and distances[new_node] == INF:
            distances[new_node] = dist + new_dist
            heapq.heappush(Q, (dist + new_dist, new_node))

print(distances[k])
    