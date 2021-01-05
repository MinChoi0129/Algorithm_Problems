case = []
print_0_cnt = [1, 0]
print_1_cnt = [0, 1]

def fill_cnts(max_num):
    global print_0_cnt, print_1_cnt
    if max_num <= 1:
        return
    for _ in range(max_num):
        print_0_cnt.append(print_1_cnt[-1])
        print_1_cnt.append(print_1_cnt[-1] + print_1_cnt[-2])


T = int(input())
for _ in range(T):
    case.append(int(input()))

fill_cnts(max(case))

for i in case:
    print(print_0_cnt[i], print_1_cnt[i])