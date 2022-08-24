a, b = map(int, input().split())
x, y = map(int, input().split())
answer, guessable = [], True
for num in range(a, b + 1):
    if num % x == y:
        answer.append(num)
    if len(answer) == 2:
        guessable = False
        break
print(answer[0] if guessable else "Unknown Number")