n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
from time import sleep
import os
    
def tryMode(color, rotate):
    print("=============================")
    if color == "blue":
        if rotate == 0:
            dx = [0] # 모드별 수정
            dy = [0, 1, 2, 3] # 모드별 수정
            maxSum = 0
            while True:
                sleep(0.5)
                tmpSum = 0
                for x in dx: # 모드별 수정
                    for y in dy: # 모드별 수정
                        print(paper[x][y], end = " ")
                        tmpSum += paper[x][y]
                    print()
                print("tmp :", tmpSum, "VS", "max :", maxSum)
                if tmpSum > maxSum:
                    maxSum = tmpSum
                

                if dy[-1] + 1 <= m - 1:
                    for i in range(len(dy)):
                        dy[i] += 1
                
                else:
                    dy = [0, 1, 2, 3] # 모드별 수정
                    if dx[-1] + 1 <= n - 1:
                        for i in range(len(dx)):
                            dx[i] += 1
                    else:
                        print("최댓값 =", maxSum)
                        return maxSum
        elif rotate == 90:
            dx = [0, 1, 2, 3] # 모드별 수정
            dy = [0] # 모드별 수정
            maxSum = 0
            while True:
                sleep(0.5)
                tmpSum = 0
                for y in dy: # 모드별 수정
                    for x in dx: # 모드별 수정
                        print(paper[x][y], end = " ")
                        tmpSum += paper[x][y]
                    print()
                print("tmp :", tmpSum, "VS", "max :", maxSum)
                if tmpSum > maxSum:
                    maxSum = tmpSum
                

                if dy[-1] + 1 <= m - 1:
                    for i in range(len(dy)):
                        dy[i] += 1
                
                else:
                    dy = [0] # 모드별 수정
                    if dx[-1] + 1 <= n - 1:
                        for i in range(len(dx)):
                            dx[i] += 1
                    else:
                        print("최댓값 =", maxSum)
                        return maxSum

    if color == "yellow":
        dx = [0, 1] # 모드별 수정
        dy = [0, 1] # 모드별 수정
        maxSum = 0
        while True:
            sleep(0.5)
            tmpSum = 0
            for x in dx: # 모드별 수정
                for y in dy: # 모드별 수정
                    print(paper[x][y], end = " ")
                    tmpSum += paper[x][y]
                print()
            print("tmp :", tmpSum, "VS", "max :", maxSum)
            if tmpSum > maxSum:
                maxSum = tmpSum
            

            if dy[-1] + 1 <= m - 1:
                for i in range(len(dy)):
                    dy[i] += 1
            
            else:
                dy = [0, 1] # 모드별 수정
                if dx[-1] + 1 <= n - 1:
                    for i in range(len(dx)):
                        dx[i] += 1
                else:
                    print("최댓값 =", maxSum)
                    return maxSum

    if color == "orange":
        if rotate == 0:
            dx = [0, 1, 2] # 모드별 수정
            dy = [0] # 모드별 수정
            maxSum = 0
            while True:
                sleep(0.5)
                tmpSum = 0
                for x in dx: # 모드별 수정
                    for y in dy: # 모드별 수정
                        print(paper[x][y], end = " ")
                        tmpSum += paper[x][y]
                    print()
                print("tmp :", tmpSum, "VS", "max :", maxSum)
                if tmpSum > maxSum:
                    maxSum = tmpSum
                

                if dy[-1] + 1 <= m - 1:
                    for i in range(len(dy)):
                        dy[i] += 1
                
                else:
                    dy = [0, 1, 2, 3] # 모드별 수정
                    if dx[-1] + 1 <= n - 1:
                        for i in range(len(dx)):
                            dx[i] += 1
                    else:
                        print("최댓값 =", maxSum)
                        return maxSum
        elif rotate == 90:
            dx = [0, 1, 2, 3] # 모드별 수정
            dy = [0] # 모드별 수정
            maxSum = 0
            while True:
                sleep(0.5)
                tmpSum = 0
                for y in dy: # 모드별 수정
                    for x in dx: # 모드별 수정
                        print(paper[x][y], end = " ")
                        tmpSum += paper[x][y]
                    print()
                print("tmp :", tmpSum, "VS", "max :", maxSum)
                if tmpSum > maxSum:
                    maxSum = tmpSum
                

                if dy[-1] + 1 <= m - 1:
                    for i in range(len(dy)):
                        dy[i] += 1
                
                else:
                    dy = [0] # 모드별 수정
                    if dx[-1] + 1 <= n - 1:
                        for i in range(len(dx)):
                            dx[i] += 1
                    else:
                        print("최댓값 =", maxSum)
                        return maxSum

os.system("clear")
dx, dy = [], []
maxList = [
    tryMode("blue", 0), tryMode("blue", 90),
    tryMode("yellow", 0),
]
print("\n\nREAL MAXIMUM = ", max(maxList))