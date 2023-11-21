for _ in range(int(input())):
    A, B, C, D = map(float, input().split())
    N, M = None, 2000000
    for x in range(-M, M+1):
        if A*(x**3)+B*(x**2)+C*x+D == 0:
            N = x
            break
    X = {N}

    a, b, c = A, A*N+B, A*(N**2)+B*N+C 
    d = b**2 - 4*a*c 

    if d == 0: X.add((-b) / (2*a))
    elif d > 0: 
        x1 = ((-b) + d ** 0.5) / (2*a) 
        x2 = ((-b) - d ** 0.5) / (2*a) 
        X.add(x1)
        X.add(x2)
    
    print(*sorted(X))