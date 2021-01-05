N = int(input())
seq = input().split()
op_cnt = list(map(int, input().split()))
op = ['+' * op_cnt[0], '-' * op_cnt[1], '*' * op_cnt[2], '/' * op_cnt[3]]
# 나누기 = int(abs(a / b))

possible = []

length = len(seq)






print(max(possible))
print(min(possible))