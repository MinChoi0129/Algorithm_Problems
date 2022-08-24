T = int(input())

cpr_list = []

for _ in range(T):
    cpr_list.append(input().split())

for case in cpr_list:
    print("Distances:", end = " ")
    length = len(case[0])
    for i in range(length):
        if ord(case[1][i]) - ord(case[0][i]) >= 0:
            print(ord(case[1][i]) - ord(case[0][i]), end = " ")
        else:
            print(ord(case[1][i]) + 26 - ord(case[0][i]), end = " ")
    print()