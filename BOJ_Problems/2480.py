a, b, c = map(int, input().split())
if a == b == c:
    print(1000*a+10000)
elif a == b != c:
    print(1000 + 100 * a)
elif a == c != b:
    print(1000 + 100 * a)    
elif b == c != a:
    print(1000 + 100 * b)
elif a != b != c:
    print(max(a, b, c) * 100)