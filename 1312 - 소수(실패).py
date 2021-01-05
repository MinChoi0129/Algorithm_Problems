a, b, n = map(int, input().split())

l = str(float(a / b))

nl = l[l.find(".") + 1 : ]

try:
    print(l)
    print(nl)
    print(nl[n - 1])
except:
    print(0)