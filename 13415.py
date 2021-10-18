import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = [*map(int, input().split())]
for _ in range(int(input())):
    a, b = map(int, input().split())    
    arr = sorted(arr[:a]) + arr[a:]
    arr = sorted(arr[:b], reverse = True) + arr[b:]

for num in arr:
    print(num, end = " ")