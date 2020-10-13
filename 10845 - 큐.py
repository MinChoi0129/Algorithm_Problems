import sys

n = int(input())

def que(cmd):
    global arr
    if cmd[0] == "push":
        arr.append(cmd[1])
    elif cmd[0] == "pop":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop(0))
    elif cmd[0] == "size":
        print(len(arr))
    elif cmd[0] == "front":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    elif cmd[0] == "back":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
    elif cmd[0] == "empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    else:
        pass
    
arr = []
for _ in range(n):
    que(sys.stdin.readline().rstrip().split())
