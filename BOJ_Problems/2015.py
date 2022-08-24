n, k = map(int, input().split())

# Initializing
a = [0] + [*map(int, input().split())]
count = 0
    
for i in range(1, n + 1):
    value = a[i]
    if value == k: count += 1
    for x in range(i + 1, n + 1):
        value += a[x]
        if value == k: count += 1

print(count)