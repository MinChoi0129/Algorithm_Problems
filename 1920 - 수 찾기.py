import sys
n = int(sys.stdin.readline().rstrip())
arr = set((map(int, sys.stdin.readline().rstrip().split())))
m = int(sys.stdin.readline().rstrip())
find = list(map(int, sys.stdin.readline().rstrip().split()))

for i in find:
    if i in arr:
        print(1)
    else:
        print(0)