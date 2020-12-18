import sys
sys.setrecursionlimit(100000)  # 런타임오류 해결

possible = []
count = 0

def dfs(x, y):
    global count
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if floor[x][y] == 1:
        count += 1
        floor[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

N, M, K = map(int, sys.stdin.readline().split())

floor = [[0] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    floor[r - 1][c - 1] = 1
    
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            possible.append(count)
        count = 0
        
print(max(possible))