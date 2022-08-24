import sys, copy
sys.setrecursionlimit(10000000)

n, m = map(int, input().split())
house = [[0] * m for _ in range(n)]
holes = [[False] * m for _ in range(n)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    holes[x - 1][y - 1] = True

house[0][0] = 1

for y in range(m):
    for x in range(n):
        if (x == y == 0) or holes[x][y]:
            continue
        
        if y % 2 == 0: # 짝수
            try:
                if x - 1 >= 0 and y >= 0:
                    house[x][y] += house[x-1][y] # 위에서 내려온 것
            except: pass
            try: 
                if x >= 0 and y - 1 >= 0:
                    house[x][y] += house[x][y-1] # 왼쪽 아래에서 올라온 것
            except: pass
            try:  
                if x - 1 >= 0 and y - 1 >= 0:
                    house[x][y] += house[x-1][y-1] # 왼쪽 위에서 내려온 것
            except: pass
        else: # 홀수
            try:  
                if x - 1 >= 0 and y >= 0:
                    house[x][y] += house[x-1][y] # 위에서 내려온 것
            except: pass
            try:  
                if x + 1 >= 0 and y - 1 >= 0:
                    house[x][y] += house[x+1][y-1] # 왼쪽 아래에서 올라온 것
            except: pass
            try:  
                if x >= 0 and y - 1 >= 0:
                    house[x][y] += house[x][y-1] # 왼쪽 위에서 내려온 것
            except: pass

print(house[n-1][m-1] % 1000000007)