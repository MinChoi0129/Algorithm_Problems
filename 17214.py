polynomial = input()
statement = []

tmp = ""
i = 0
while i < len(polynomial):
    if polynomial[i] == '+' or polynomial[i] == '-':
        statement.append(tmp)
        statement.append(polynomial[i])
        tmp = ""
        i += 1
    else:
        tmp += polynomial[i]
        i += 1
statement.append(tmp)

for i in statement:
    if i == '+' or i == '-':
        print(i, end = "")
        continue

    xCount = 0
    for j in i[::-1]:
        if j == 'x':
            xCount += 1
    coeff = i[:len(i) - xCount]
    
    if xCount == 0:
        print(coeff + 'x+W', end = "")
        
    elif xCount > 0:
        newCoEff = int(coeff) // (xCount + 1)
        if newCoEff > 1:
            print(newCoEff, end = "")
        for _ in range(xCount + 1):
            print("x", end = "")