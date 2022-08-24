a = input()
if len(a) % 2 == 0: print(1 if a[:len(a) // 2] == a[len(a) // 2:][::-1] else 0)
else: print(1 if a[:len(a) // 2] == a[len(a) // 2 + 1:][::-1] else 0)