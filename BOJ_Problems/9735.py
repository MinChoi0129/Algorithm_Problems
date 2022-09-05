for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    xs = set()
    N = None
    for x in range(-1000000, 1000001):
        if a*(x**3)+b*(x**2)+c*x+d == 0:
            N = x; break
 
    A, B, C = a, a*N+b, a*(N**2)+b*N+c
    D = B**2 - 4*A*C
    if D == 0: xs.add((-B) / (2*A))
    elif D > 0:
        x1, x2 = ((-B) + D ** 0.5) / (2*A), ((-B) - D ** 0.5) / (2*A)
        xs.add(x1)
        xs.add(x2)
    xs.add(N)
    for x in sorted(xs): print("%.4f" % x, end = " ")
    print()