def nCr(n, r): # 4C3
    if n == 0 or n == r or r == 0:
        return 1
    else:
        pascal = [[1] * (n + 1) for _ in range(0, n + 1)]
        for x in range(1, n + 1):
            for y in range(1, x):
                pascal[x][y] = pascal[x-1][y-1] + pascal[x-1][y]
        return pascal[n][r]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(nCr(m, n))