import sys
from collections import Counter

def 산술평균(num):
    return round(sum(num) / len(num))
    

def 중앙값(num):
    if len(num) == 1:
        return num[0]
    else:
        return num[(len(num) + 1) // 2 - 1]

def 최빈값(num):
    if len(num) == 1:
        return num[0]
    else:
        cnt = Counter(num).most_common(2)
        if cnt[0][1] == cnt[1][1]:
            return cnt[1][0]
        else:
            return cnt[0][0]
    
    
def 범위(num):
    if len(num) == 1:
        return 0
    else:
        return num[len(num) -1] - num[0]
    

n = int(sys.stdin.readline())
num = sorted([int(sys.stdin.readline()) for i in range(n)])

print(산술평균(num))
print(중앙값(num))
print(최빈값(num))
print(범위(num))