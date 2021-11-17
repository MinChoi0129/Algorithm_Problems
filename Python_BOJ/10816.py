import sys
n = int(sys.stdin.readline().rstrip())
num = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
find = list(map(int, sys.stdin.readline().rstrip().split()))

status = {}

for i in num:
    if i not in status:
        status[i] = 1
    else:
        status[i] += 1
        
for i in find:
    if i in status:
        print(status[i], end = " ")
    else:
        print(0, end = " ")