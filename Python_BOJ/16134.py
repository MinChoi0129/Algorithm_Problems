def getPowerWithModP(b, e, p):
    result = 1
    while e:
        if e % 2 == 1: result = (result * b) % p
        e //= 2
        b = (b ** 2) % p
    return result

n, r = map(int, input().split())

factorials, p = [1], 1000000007
for i in range(1, n + 1): factorials.append((factorials[-1] * i) % p)

left = factorials[n] % p
right = getPowerWithModP(factorials[r] * factorials[n-r], p-2, p)

'''
1. (A*B가 너무 커서, 특히 B가 너무 커서 모듈러 연산을 사용해야함.)
2. A*B % p = (A % p * B % p) % p
3. left = A % p, right = B % p 
'''
print((left * right) % p)