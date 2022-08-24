n, m, r = map(int, input().split())
locations = dict({i+1:value for i, value in enumerate(map(int, input().split()))})
floyd_warshall = [[int(1e9)] * n for _ in range(n)]
for _ in range(r):
    a, b, l = map(int, input().split())
    floyd_warshall[a-1][b-1] = floyd_warshall[b-1][a-1] = l
for center in range(n):
    for node1 in range(n):
        for node2 in range(n):
            if node1 == node2: floyd_warshall[node1][node2] = 0
            else: floyd_warshall[node1][node2] = min(floyd_warshall[node1][node2], floyd_warshall[node1][center] + floyd_warshall[center][node2])
print(max([sum([locations[y+1] for y in range(n) if floyd_warshall[x][y] <= m]) for x in range(n)]))

# i=lambda:map(int,input().split())
# n,m,r=i()
# R,*p=range(n),*i()
# f=[[1e9]*n for _ in R]
# for _ in range(r):a,b,l=i();f[a-1][b-1]=f[b-1][a-1]=l
# for c in R:
#  f[c][c]=0
#  for d in R:
#   for e in R:f[d][e]=min(f[d][e],f[d][c]+f[c][e])
# print(max([sum([p[y]for y in R if f[x][y]<=m])for x in R]))