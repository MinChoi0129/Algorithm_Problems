import sys, heapq
input = lambda : sys.stdin.readline().rstrip()

v, e = map(int, input().split())
connections = {}
for _ in range(e):
    a, b, c = map(int, input().split())
    if a not in connections: connections[a] = [(b, c)]
    else: connections[a].append((b, c))

    if b not in connections: connections[b] = [(a, c)]
    else: connections[b].append((a, c))

visited = [None] + [False] * v
heap, body_length, sum_of_edges = [(0, 1)], 0, 0 # heap: (edge, node)

while body_length < v:
    edge, node = heapq.heappop(heap)
    if not visited[node]:
        visited[node] = True
        sum_of_edges += edge
        body_length += 1
        for new_node, new_edge in connections[node]:
            if not visited[new_node]: # 메모리, 시간 모두 절약 가능
                heapq.heappush(heap, (new_edge, new_node))

print(sum_of_edges)