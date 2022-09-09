n = int(input())
table = [[*map(int, input().split())] for _ in range(n)]
for i in range(n-1):
    for j in range(3): table[i+1][j] += min(table[i][(j+1) % 3], table[i][(j+2) % 3])
print(min(table[-1]))