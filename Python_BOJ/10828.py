import sys
n = int(input())
stack = []
def show(arr):
    if arr == "top":
        try:
            print(stack[-1])
        except:
            print(-1)
    elif arr == "size":
        print(len(stack))
    elif arr == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif arr == "pop":
        try:
            print(stack.pop())
        except:
            print(-1)
    else:
        arr = arr.split()
        stack.append(arr[1])
        

for _ in range(n):
    show(sys.stdin.readline().rstrip())