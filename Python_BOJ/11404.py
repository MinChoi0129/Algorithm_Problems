import sys
input = lambda : sys.stdin.readline().rstrip()
INF = sys.maxsize
n, m = int(input()), int(input())
floyd_warshall = [[INF] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    floyd_warshall[a-1][b-1] = min(floyd_warshall[a-1][b-1], c)
    
for center in range(n):
    for node1 in range(n):
        for node2 in range(n):
            if node1 == node2: floyd_warshall[node1][node2] = 0
            else: floyd_warshall[node1][node2] = min(floyd_warshall[node1][node2], floyd_warshall[node1][center] + floyd_warshall[center][node2])

for line in floyd_warshall:
    for element in line:
        print(element if element != INF else 0, end = " ")
    print()