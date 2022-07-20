from collections import deque

negatives, positives, grouped_negatives, grouped_positives = [], [], deque(), deque()

n, m = map(int, input().split())
for num in map(int, input().split()):
    if num < 0: negatives.append(num)
    else: positives.append(num)
    
negatives.sort(reverse=True); positives.sort()

# negatives
while negatives:
    tmp = []
    for _ in range(m):
        try: tmp.append(negatives.pop())
        except: pass
    grouped_negatives.append(tmp)
    
# positives
while positives:
    tmp = []
    for _ in range(m):
        try: tmp.append(positives.pop())
        except: pass
    grouped_positives.append(tmp)

distance = 0
while grouped_negatives or grouped_positives:
    ns, ps = len(grouped_negatives), len(grouped_positives)
    
    if ns + ps == 1: # 편도
        if len(grouped_negatives) == 0: distance += grouped_positives.popleft()[0]
        else: distance += abs(grouped_negatives.pop()[0])
    elif (ns == 0 and ps > 1) or (ps == 0 and ns > 1): # 남은 한쪽으로 계속 시도
        if ns == 0: # 오른쪽만 남음
            while len(grouped_positives) > 1: distance += (2 * grouped_positives.pop()[0])
        else: # 왼쪽만 남음
            while len(grouped_negatives) > 1: distance += (2 * abs(grouped_negatives.pop()[0]))
    else: # 왕복
        left, right = abs(grouped_negatives[-1][0]), grouped_positives[0][0]
        if left < right: distance += (2 * abs(grouped_negatives.pop()[0]))
        else: distance += (2 * grouped_positives.popleft()[0])

print(distance)