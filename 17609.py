import sys, copy
input = lambda : sys.stdin.readline().rstrip()

def check(string : list):
    
    # check 0
    palindrome = 0
    start, end = 0, len(string) - 1
    while start < end:
        if string[start] != string[end]:
            return 1
        start += 1
        end -= 1
    if palindrome == 0:
        return palindrome
    
    
    # check 1
    possibles = []
    for i in range(len(string)):
        copyString = copy.deepcopy(string)
        copyString.pop(i)
        possibles.append(copyString)
        
    for possible in possibles:
        length = len(possible)
        if length % 2 == 0:
            if possible[ : length // 2] == list(reversed(possible[length // 2 : ])):
                return 1
        else:
            if possible[ : length // 2] == list(reversed(possible[length // 2 + 1 : ])):
                return 1
    return 2

for _ in range(int(input())):
    print(check(list(input())))