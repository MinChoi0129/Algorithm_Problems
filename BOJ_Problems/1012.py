import sys
sys.setrecursionlimit(100000) # 런타임오류 해결

farm = []

def dfs(x, y, N, M):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    
    if farm[x][y] == 1:
        farm[x][y] = 0
        dfs(x - 1, y, N, M)
        dfs(x, y - 1, N, M)
        dfs(x + 1, y, N, M)
        dfs(x, y + 1, N, M)
        return True
    return False

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    farm = [[0 for _ in range(M)] for _ in range(N)] # T회 실행되므로 매번 농장을 초기화
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        farm[y][x] = 1 # x축 >> ; y축 vv ; 이차원배열과 축이 반대
        
    result = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j, N, M):
                result += 1
                
    print(result)