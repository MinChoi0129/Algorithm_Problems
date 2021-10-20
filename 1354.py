import sys
sys.setrecursionlimit(100000000)
n, p, q, x, y = map(int, input().split())

a = dict()

def dfs(num : str):
    try:
        return 1 if int(num) <= 0 else a[num]
    except:
        a[num] = dfs(str(int(num) // p - x)) + dfs(str(int(num) // q - y))
        return a[num]

print(dfs(str(n)))