import sys

txt = sys.stdin.readline().rstrip()
bang = sys.stdin.readline().rstrip()
length = len(bang)
tmp = []
for c in txt:
    tmp.append(c)
    if len(tmp) >= length:
        if ''.join(tmp[-length:]) == bang:
            for _ in range(length):
                tmp.pop()

print(''.join(tmp)) if tmp else print("FRULA")