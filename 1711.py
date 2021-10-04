import sys
input = lambda : sys.stdin.readline().rstrip()

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

allPoints = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    allPoints.append([a, b])

count = 0
for i in range(len(allPoints)):
    for j in range(i + 1, len(allPoints)):
        for k in range(j + 1, len(allPoints)):
            if isRightTriangle(allPoints[i], allPoints[j], allPoints[k]):
                count += 1
print(count)