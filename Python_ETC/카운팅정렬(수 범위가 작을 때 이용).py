import sys

n = int(sys.stdin.readline())

arr = [0 for _ in range(10001)]

for i in range(n):
    get = int(sys.stdin.readline())
    arr[get] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)