e, s, m = map(int, input().split())

year = 1
base_e, base_s, base_m = 1, 1, 1

while True:
    if base_e == e and base_s == s and base_m == m:
        print(year)
        break
    
    year += 1
    base_e += 1
    base_s += 1
    base_m += 1
    
    if base_e == 16:
        base_e = 1
        
    if base_s == 29:
        base_s = 1
        
    if base_m == 20:
        base_m = 1