n = int(input())
chemicals = sorted(map(int, input().split()))


answer_a, answer_b, value_close_to_zero = 1e11, 1e11, 1e11
p1, p2 = 0, n - 1

while p1 < p2:
    a, b = chemicals[p1], chemicals[p2]
    mixed = a + b
    if value_close_to_zero > abs(mixed):
        answer_a, answer_b = a, b
        value_close_to_zero = abs(mixed)
    
    if mixed < 0: p1 += 1
    else: p2 -= 1

print(answer_a, answer_b)