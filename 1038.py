n = int(input())

descendingNumbers = []

def isDescending(num):
    if len(num) == 1:
        return True
    
    else:
        before = int(num[0])
        for i in range(1, len(num)):
            if int(num[i]) >= before:
                return False
        return True

num = 0
while True:
    if isDescending(str(num)):
        descendingNumbers.append(num)
    if len(descendingNumbers) > n:
        break
    if num > 987654321:
        break
    num += 1


if len(descendingNumbers) == n + 1:
    print(descendingNumbers[n])
else:
    print(-1)