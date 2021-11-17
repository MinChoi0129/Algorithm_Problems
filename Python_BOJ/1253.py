n = int(input())
numbers = sorted(map(int, input().split()))

def isGood(numbersWithoutTheNum, theNum):
    lastIdx = len(numbersWithoutTheNum) - 1
    p1, p2 = 0, lastIdx
    while p1 < p2:
        result = numbersWithoutTheNum[p1] + numbersWithoutTheNum[p2]
        if result == theNum:
            return True
        
        if result < theNum:
            p1 += 1
        else:
            p2 -= 1
            
    return False

count = 0
for i in range(len(numbers)):
    if isGood(numbers[:i] + numbers[i+1:], numbers[i]): count += 1

print(count)