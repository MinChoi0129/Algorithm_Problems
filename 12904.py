s, t = input(), input()

while len(s) != len(t):
    if t[-1] == 'A':
       t = t[:-1] 
    elif t[-1] == 'B':
        t = t[:-1]
        t = t[::-1]

print(1) if s == t else print(0)