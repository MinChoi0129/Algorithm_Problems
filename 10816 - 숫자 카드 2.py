import sys
n = int(sys.stdin.readline().rstrip())
card = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
find = list(map(int, sys.stdin.readline().rstrip().split()))
count = [0 for _ in range(m)]

index = 0
for i in find:
    if i in card:
        count[index] += 1
    index += 1
    
print(count)