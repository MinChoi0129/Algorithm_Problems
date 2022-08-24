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
if '' in statement:
    statement.pop(0)

for i in statement:
    if i == '+' or i == '-':
        print(i, end = "")
        continue
    
    if i == '0':
        print("W", end = "")
    
    else:
        xCount = 0
        for j in i:
            if j == 'x':
                xCount += 1
        coEff = int(i[ : len(i) - xCount])
                
        if xCount == 0:
            if coEff == 1:
                print('x+W', end = "")
            else:
                print(str(coEff) + 'x+W')
        
        else:
            integralCoEff = str(coEff // (xCount + 1))
            if integralCoEff == '1':
                print('x' * (xCount + 1), end = "")
            else:
                print(integralCoEff, end = "")
                print('x' * (xCount + 1), end = "")

if statement[-1] not in [str(i) for i in range(1, 10001)] and statement[-1] != '0':
    print("+W", end = "")