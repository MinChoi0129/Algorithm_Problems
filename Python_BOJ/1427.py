n = input()

a = [0 for _ in range(len(n))]

for i in range(len(n)):
    a[i] = n[i]

a.sort(reverse=True)
for i in range(len(a)):
    print(a[i], end="")