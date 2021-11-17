import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
p1, p2 = 0, 1

minDiffernce = 1e15
while p1 < n and p2 < n:
    diff = arr[p2] - arr[p1]
    if diff == m:
        print(m)
        exit(0)
        
    if diff < m:
        p2 += 1
    else:
        minDiffernce = min(minDiffernce, diff)
        p1 += 1 

print(minDiffernce)