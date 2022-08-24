import sys
input = lambda : sys.stdin.readline().rstrip()
from itertools import permutations as P
n = int(input())
numbers = input().split()
tmp = [*map(int, input().split())]

def cal(statement):
    result = statement[0]
    lastIdx = len(statement) - 1
    i = 1
    while i <= lastIdx:
        if statement[i] == '+':
            i += 1
            result += statement[i]
            i += 1
        elif statement[i] == '-':
            i += 1
            result -= statement[i]
            i += 1
        elif statement[i] == '*':
            i += 1
            result *= statement[i]
            i += 1
        elif statement[i] == '/':
            i += 1
            if result >= 0:
                result //= statement[i]
                i += 1
            else:
                result *= -1
                result //= statement[i]
                result *= -1
                i += 1
    return result
            
operator = []
for i in range(len(tmp)):
    for j in range(tmp[i]):
        if i == 0:
            operator.append('+')
        elif i == 1:
            operator.append('-')
        elif i == 2:
            operator.append('*')
        else:
            operator.append('/')
                        
allStatements = []
combiOperators = list(set(P(operator, len(operator))))
for i in combiOperators:
    tmpStatement = [int(numbers[0])]
    for j in range(1, n):
        tmpStatement.append(i[j - 1])
        tmpStatement.append(int(numbers[j]))
    allStatements.append(tmpStatement)

minResult, maxResult = 10000000001, -10000000001
for i in allStatements:
    calResult = cal(i)
    minResult = min(minResult, calResult)
    maxResult = max(maxResult, calResult)

print(maxResult)
print(minResult)