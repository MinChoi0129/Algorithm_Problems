n, letters = int(input()), set()

for palin in input().split():
    letters.add(palin[0])

print(1) if len(letters) == 1 else print(0)