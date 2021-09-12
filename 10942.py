import sys

n = int(input())
seq = list(map(int, input().split()))
isPalindrome = [[0] * (n + 1) for _ in range(n + 1)]
seq.insert(0, 0)

for i in range(1, n + 1):
    isPalindrome[i][i] = 1

for i in range(1, n):
    if seq[i] == seq[i + 1]:
        isPalindrome[i][i + 1] = 1

for i in range(n - 2, 0, -1):
    for j in range(i + 2, n + 1):
        if seq[i] == seq[j] and isPalindrome[i + 1][j - 1]:
            isPalindrome[i][j] = 1

for _ in range(int(input())):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    print(isPalindrome[s][e])