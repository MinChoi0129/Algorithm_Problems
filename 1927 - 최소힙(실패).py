import sys

arr = []
order = []

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    order.append(int(sys.stdin.readline().rstrip()))
    
for num in order:
    if num == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(arr.pop(0))
    else:
        arr.append(num)
        arr.sort()