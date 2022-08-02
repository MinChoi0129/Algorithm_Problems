from itertools import permutations as P

def isAntiPalindrome(case, size):
    for i in range(size // 2):
        if case[i] == case[size - 1 - i]: return False
    return True
    

def main():
    text = input()
    size = len(text)
    for case in P(sorted(text)):
        # print(case)
        if isAntiPalindrome(case, size):
            print(''.join(case))
            return
    print(-1)
    
main()