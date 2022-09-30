from itertools import combinations_with_replacement as H
n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
for case in sorted(set(H(arr, m))):
    print(*case)