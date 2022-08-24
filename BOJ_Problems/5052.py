import sys
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    a = list(sorted([input() for _ in range(int(input()))]))
    conditional = True
    for i in range(len(a) - 1):
        if a[i + 1].startswith(a[i]):
            conditional = False
            break
    print("YES" if conditional else "NO")