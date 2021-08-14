import sys
input = lambda : sys.stdin.readline().rstrip()

def tryJump(jumpWay):
    idx, total = -1, 0
    for jump in jumpWay:
        idx += jump
        total += stairs[idx]
    return total

def issublist(small, big):
    a, b = "", ""

    for i in small:
        a += str(i)
    
    for i in big:
        b += str(i)

    return True if a in b else False

def isFit(lst):
    if issublist([1, 1, 1], lst):
        return False
    if issublist([2, 1, 1], lst):
        return False
    for step in lst:
        if step >= 3:
            return False
    return True

def NaturalNumberDivisor(n):
    def generator(n):
        a = [0 for i in range(n + 1)]
        k = 1
        y = n - 1
        while k != 0:
            x = a[k - 1] + 1
            k -= 1
            while 2 * x <= y:
                a[k] = x
                y -= x
                k += 1
            l = k + 1
            while x <= y:
                a[k] = x
                a[l] = y
                rtn1 = a[:k + 2]
                if isFit(rtn1):
                    yield rtn1
                x += 1
                y -= 1
            a[k] = x + y
            y = x + y - 1
            rtn2 = a[:k + 1]
            if isFit(rtn2):
                yield rtn2

    return list(generator(n))


n, maxSum = int(input()), 0
# stairs = [int(input()) for _ in range(n)]

# for jumpWay in NaturalNumberDivisor(n):
#     result = tryJump(jumpWay)
#     maxSum = result if maxSum < result else maxSum

# print(maxSum)
print(NaturalNumberDivisor(n))