import sys, math
input = lambda : sys.stdin.readline().rstrip()
from itertools import combinations as C

def isRightTriangle(Pa, Pb, Pc):
    vecAB = (Pb[0]-Pa[0], Pb[1]-Pa[1])
    vecBA = (-Pb[0]+Pa[0], -Pb[1]+Pa[1])
    
    vecAC = (Pc[0]-Pa[0], Pc[1]-Pa[1])
    vecCA = (-Pc[0]+Pa[0], -Pc[1]+Pa[1])
    
    vecBC = (Pc[0]-Pb[0], Pc[1]-Pb[1])
    vecCB = (-Pc[0]+Pb[0], -Pc[1]+Pb[1])
    
    
    if vecAB[0] * vecAC[0] + vecAB[1] * vecAC[1] == 0: # A기준
        return True
    if vecBA[0] * vecBC[0] + vecBA[1] * vecBC[1] == 0: # B기준
        return True
    if vecCA[0] * vecCB[0] + vecCA[1] * vecCB[1] == 0: # C기준
        return True
    return False
    
allPoints = [[*map(int, input().split())] for _ in range(int(input()))]
allPoints.sort()
count = 0
for Pa, Pb, Pc in C(allPoints, 3):
    if isRightTriangle(Pa, Pb, Pc):
        count += 1
print(count)