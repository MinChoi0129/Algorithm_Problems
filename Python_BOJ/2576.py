a = [int(input()) for _ in range(7)]
b = []
for i in a:
    if i % 2 == 1:
        b.append(i)

if len(b) != 0:
    print(sum(b))
    print(min(b))
else:
    print(-1)