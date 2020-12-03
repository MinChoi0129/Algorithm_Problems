a, b, n = map(int, input().split())

l = str(float(a / b))

if len(l) - (l.find('.') + 1) >= n:
    print(l[l.find('.') + n])
else:
    print(0)
