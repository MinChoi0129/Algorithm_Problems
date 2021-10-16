import sys
sys.setrecursionlimit(100000000)

n = int(input())
log = dict()

def dp(day_count, late, absent):
    if late >= 2 or absent >= 3:
        return 0
    
    if day_count == n:
        return 1
    
    try:
        return log[(day_count, late, absent)]
    except:
        # 다음 날의 정상등교case + 지각case + 결석case 중 조건의 만족하는 것들의 합
        log[(day_count, late, absent)] = \
            dp(day_count + 1, late, 0) + \
            dp(day_count + 1, late + 1, 0) + \
            dp(day_count + 1, late, absent + 1)
            # 정상 등교(연속결석 카운트 리셋)
            # 지각(연속결석 카운트 리셋)
            # 결석(연속결석 카운트 1 증가)
        return log[(day_count, late, absent)]

print(dp(0, 0, 0) % 1000000)