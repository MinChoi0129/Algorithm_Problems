def myEval(statement):
    if '+' not in statement:
        return int(statement)
    else:
        sum = 0
        for number in statement.split('+'):
            sum += int(number)
        return sum

sepCal = [-myEval(i) for i in input().split('-')]
sepCal[0] *= -1
print(sum(sepCal))