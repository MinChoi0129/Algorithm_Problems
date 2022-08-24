n, k = map(int, input().split())
a = [0 for i in range(n)]
b = [0 for i in range(n)]
for i in range(n):
    a[i] = int(input())
a.reverse()
sum = 0
for i in range(n):
    b[i] = k // a[i] #몫
    k = k % a[i]
    sum += b[i]

print(sum)