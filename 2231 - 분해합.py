import sys

def find_old_num(new_num):
    for i in range(1, new_num + 1):
        string_i = str(i)
        sum = i
        for j in range(len(string_i)):
            sum += int(string_i[j])
        if new_num == sum:
            return i
    return 0

new_num = int(sys.stdin.readline().rstrip())

print(find_old_num(new_num))