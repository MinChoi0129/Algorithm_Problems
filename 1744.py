from collections import deque

arr = [int(input()) for i in range(int(input()))]
positive, negative = [], []

answer = 0
for num in arr:
    if num > 1: positive.append(num)
    elif num == 1: answer += 1
    else: negative.append(num) # 0은 음수쪽으로 들어감

positive, negative = deque(sorted(positive, reverse=True)), deque(sorted(negative))

while len(positive) >= 2 or len(negative) >= 2:
    if len(positive) >= 2: answer += positive.popleft() * positive.popleft()
    if len(negative) >= 2: answer += negative.popleft() * negative.popleft()

if positive: answer += positive[0]
if negative: answer += negative[0]

print(answer)