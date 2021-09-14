import sys, copy
input = lambda : sys.stdin.readline().rstrip()

def check(string : list):
    
    # check 0
    palindrome = 0
    start, end = 0, len(string)
    while start < end:
        if string[start] != string[end]:
            palindrome = 1
            break
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
        start, end = 0, len(possible)
        while start < end:
            if possible[start] != possible[end]:
                break
            start += 1
            end -= 1
        return 1
    return 2
    

for _ in range(int(input())):
    check(list(input()))