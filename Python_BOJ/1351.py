n, p, q = map(int, input().split())

a = dict()
a[0] = 1

def dfs(num):
    try:
        return a[num]
    except:
        a[num] = dfs(num // p) + dfs(num // q)
        return a[num]

print(dfs(n))