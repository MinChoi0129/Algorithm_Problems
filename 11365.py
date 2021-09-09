txts = []

while True:
    txt = input()
    if txt == "END":
        break
    else:
        txts.append(txt)

for txt in txts:
    print(''.join(reversed(txt)))