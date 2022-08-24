n = int(input())
a = list(map(int, input().split()))
a.sort() # 1 2 3 3 4
b = []
b.append(a[0])
for i in range(1, n): # 1<= <=4
    b.append(b[i - 1] + a[i])

sum = 0
for i in range(n):
    sum += b[i]
print(sum)