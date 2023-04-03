for _ in range(int(input())): # 각 테스트케이스 마다
    A, B, C, D = map(int, input().split()) # 3차 방정식 계수
    모든_근 = set()

    N = None # 정수 근
    for x in range(-1000000, 1000001): # 정수 근은 하나 이상 존재한다.
        if A*(x**3)+B*(x**2)+C*x+D == 0:
            N = x
            break
    모든_근.add(N)

    a, b, c = A, A*N+B, A*(N**2)+B*N+C # 조립제법을 이용하여 구한 나머지 2차방정식 계수
    판별식 = b**2 - 4*a*c # 이차방정식의 판별식 D

    if 판별식 == 0: 모든_근.add((-b) / (2*a)) # 접하면(중근이면)
    elif 판별식 > 0: # 교점이 2개면(서로 다른 두 근을 가지면)
        x1 = ((-b) + 판별식 ** 0.5) / (2*a) # 근의 공식
        x2 = ((-b) - 판별식 ** 0.5) / (2*a) # 근의 공식
        모든_근.add(x1)
        모든_근.add(x2)
    else: # 허근이면 문제 상황과 관련 없음
        pass
    
    for x in sorted(모든_근): # 오름차순
        print("%.4f" % x, end = " ")
    print()

