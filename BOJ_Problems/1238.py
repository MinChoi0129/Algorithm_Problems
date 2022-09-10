import sys, heapq
input = lambda : sys.stdin.readline().rstrip()
INF = int(1e9)

def dijkstra(start_node, *args):
    connection, n = args

    visited = [None] + [False] * n
    distances = [None] + [INF] * n; distances[start_node] = 0

    Q = [(0, start_node)]
    while Q:
        distance, current_node = heapq.heappop(Q)
        if not visited[current_node]:
            for node, dist in connection[current_node]:
                cost = distances[current_node] + dist

                if cost < distances[node]:
                    distances[node] = cost
                    heapq.heappush(Q, (cost, node))
            visited[current_node] = True
    return distances

def main():
    n, m, x = map(int, input().split())
    connection = {i+1: [] for i in range(n)}

    for _ in range(m):
        from_node, to_node, time = map(int, input().split())
        connection[from_node].append((to_node, time))

    answer = [0] * n
    for start_node in range(1, n+1):
        result = dijkstra(start_node, connection, n)
        if start_node == x:
            for i in range(n):
                answer[i] += result[1:][i]
        answer[start_node - 1] += result[x]
    print(max(answer))

main()