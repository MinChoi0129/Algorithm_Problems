import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

pokemon = dict()

for i in range(1, n):
    pokemon[str(i)] = sys.stdin.readline().rstrip()

for i in range(m):
    question = sys.stdin.readline().rstrip()
    