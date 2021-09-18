import sys, copy
input = lambda : sys.stdin.readline().rstrip()

def check1(string : list):
    
    start, end = 0, len(string) - 1
    while start < end:
        if string[start] != string[end]:
            return min(check2(string[start : end]), check2(string[start + 1 : end + 1]))
        start += 1
        end -= 1
    return 0

def check2(string : list):
    start, end = 0, len(string) - 1
    while start < end:
        if string[start] != string[end]:
            return 2
        start += 1
        end -= 1
    return 1
    
for _ in range(int(input())):
    print(check1(list(input())))