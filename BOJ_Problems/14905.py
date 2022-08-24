def getFourPrimesForNum(n): # 8 이상의 자연수
    ans, n = (['2', '3'], n-5) if n%2 == 1 else (['2', '2'], n-4)
    for i in range(2, size+1):
        if is_primes[i] and is_primes[n-i]: return ' '.join(ans + [str(i), str(n-i)])

ns = []
while True:
    try: ns.append(int(input()))
    except: break
    
is_primes = [False, False]+[True]*(max(ns) - 1)
size = int(len(is_primes)**0.5)+1

for i in range(2, size):
    if is_primes[i]:
        for j in range(i+i, len(is_primes), i):
            is_primes[j] = False
        
for n in ns:
    if n < 8: print("Impossible.")
    else: print(getFourPrimesForNum(n))