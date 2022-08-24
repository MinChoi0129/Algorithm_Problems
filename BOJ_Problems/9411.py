from decimal import Decimal, getcontext
getcontext().prec = 100
for _ in range(int(input())):
    numbers = []
    while True:
        number = input()
        if number == '0': break
        numbers.append(Decimal(number))
    result = Decimal('000000000000000000000000000000.0000000000000000000000000000000')
    for number in numbers: result += number
    result = list(str(result))
    while result[-1] == '0':
        result.pop()
    print(''.join(result))