import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
db = dict()
for _ in range(n):
    link, pw = sys.stdin.readline().rstrip().split()
    db[link] = pw
for _ in range(m):
    link = sys.stdin.readline().rstrip()
    print(db[link])