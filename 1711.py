import sys, math
input = lambda : sys.stdin.readline().rstrip()
from itertools import combinations as C

def isRightTriangle(points):
    abab = int((points[0][0] - points[1][0]) ** 2) + int((points[0][1] - points[1][1]) ** 2)
    bcbc = int((points[1][0] - points[2][0]) ** 2) + int((points[1][1] - points[2][1]) ** 2)
    caca = int((points[2][0] - points[0][0]) ** 2) + int((points[2][1] - points[0][1]) ** 2)
    longest = max(abab, bcbc, caca)
    if longest == abab:
        if abab == bcbc + caca:
            return True
    elif longest == bcbc:
        if bcbc == abab + caca:
            return True
    elif longest == caca:
        if caca == abab + bcbc:
            return True
    return False
    
allPoints = [[*map(int, input().split())] for _ in range(int(input()))]
count = 0
while allPoints:
    Pa = allPoints.pop()
    PbPcs = list(C(allPoints, 2))
    for Pb, Pc in PbPcs:
        test = [Pa, Pb, Pc]
        if isRightTriangle(test):
            count += 1
print(count)