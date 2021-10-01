from itertools import combinations as C

l, c = map(int, input().split())
alphabets = input().split()

def check(case):
    consonantCount, vowelCount = 0, 0
    for char in case:
        if char in "aeiou": vowelCount += 1
        else: consonantCount += 1
    return False if consonantCount < 2 or vowelCount < 1 else True
    
passwords = []
for case in C(alphabets, l):
    tmp = ''.join(sorted([*case]))
    if check(tmp): passwords.append(tmp)

for i in sorted(passwords):
    print(i)