n, m, x = map(int, input().split())

connection = {i+1: [] for i in range(n)}
for _ in range(m):
    start, end, time = map(int, input().split())
    connection[start].append((end, time))
print(connection)