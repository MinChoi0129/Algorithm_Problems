from math import pow as new_pow

def find_n(e, s, p):
    if s == p: return 1
    if new_pow(e, s / e) < p: return -1

    old = -1;
    for x in range(2, s):
        new = new_pow(s / x, x);
        if old > new: return -1
        if new >= p: return x
        old = new;

e, s, p = 2.7182818459045, *map(int, input().split())
print(find_n(e, s, p))