import sys
text = input()
n = len(text)

def isPalindrome(txt):
    length = len(txt)
    if length == 1: return True
    else:
        if length % 2 == 0: return True if txt[:length // 2] == txt[length // 2:][::-1] else False
        else: return True if txt[:length // 2] == txt[length // 2 + 1:][::-1] else False
                

for length in range(n, -1, -1):
    if length == 0: print(-1)
    else:
        for step in range(n - length + 1):
            tmp_txt = text[step:step + length]
            if not isPalindrome(tmp_txt):
                print(length)
                sys.exit()