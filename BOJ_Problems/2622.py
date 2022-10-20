n = int(input())
count = 0
for i in range(1, n-1):
    for j in range(i, n-1):
        if 2*(i+j) > n >= i+2*j: count += 1
print(count)