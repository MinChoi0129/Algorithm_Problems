txt = list(input())

if '0' not in txt:
    print(-1)

else:
    cal = int(''.join(sorted(txt, reverse=True)))
    print(-1) if cal % 3 != 0 else print(cal)