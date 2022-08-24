n, m = map(int, input().split())
floyd_warshall = [[5000] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    floyd_warshall[a-1][b-1] = floyd_warshall[b-1][a-1] = 1

for center in range(n):
    for node1 in range(n):
        for node2 in range(n):
            if node1 == node2: floyd_warshall[node1][node2] = 0
            else: floyd_warshall[node1][node2] = min(floyd_warshall[node1][node2], floyd_warshall[node1][center] + floyd_warshall[node2][center])

print(sorted([[i, sum(floyd_warshall[i])] for i in range(n)], key = lambda x:x[1])[0][0] + 1)