import sys
input = lambda : sys.stdin.readline().rstrip()
n, m = map(int, input().split())
number = [*map(int, input().split())]

addedNumber = [0]

for i in range(n):
    addedNumber.append(addedNumber[-1] + number[i])
for _ in range(m):
    i, j = map(int, input().split())
    print(addedNumber[j] - addedNumber[i-1])