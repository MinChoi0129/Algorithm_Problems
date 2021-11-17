n, k = map(int, input().split())
kids = [*map(int, input().split())]

diff = []

for i in range(n - 1):
    diff.append(kids[i+1] - kids[i])

diff.sort()
print(kids[-1] - kids[0] - sum(diff[n-k:])) 