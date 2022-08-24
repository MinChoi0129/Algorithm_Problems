import sys
k = int(sys.stdin.readline().rstrip())

num = []

for _ in range(k):
    get = int(sys.stdin.readline().rstrip())
    if get == 0:
        num.pop()
    else:
        num.append(get)
print(sum(num))