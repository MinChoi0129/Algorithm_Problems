n, m = map(int, input().split())
S, M = {input() for _ in range(n)}, [input() for _ in range(m)]
cnt = 0
for i in M:
    if i in S:
        cnt += 1
print(cnt)