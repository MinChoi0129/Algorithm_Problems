txt = input()
tails = []

for i in range(len(txt)):
    tails.append(txt[i:])

for i in sorted(tails):
    print(i)