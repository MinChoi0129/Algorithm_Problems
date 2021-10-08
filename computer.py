f = open("computer.txt", mode = 'r', encoding='utf-8')
parts = {}

while True:
    line = f.readline().rstrip()
    if not line: break
    
    partsType, price = line.split()
    model = f.readline().rstrip()
    link = f.readline().rstrip()
    parts[partsType] = [int(price), model, link.split(".")[1], link]
    f.readline()

_11st, _coupang, _tmon = set(), set(), set()

totalPrice = 0
for partList in parts.values():
    if partList[2] == '11st': _11st.add(partList[3])
    elif partList[2] == 'coupang': _coupang.add(partList[3])
    elif partList[2] == 'tmon': _tmon.add(partList[3])

    totalPrice += partList[0]

print("11번가 :", len(_11st))
print("쿠팡 :", len(_coupang))
print("티몬 :", len(_tmon))
print(totalPrice, "원", sep = "")

f.close()