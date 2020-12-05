import sys
input = lambda : sys.stdin.readline().rstrip()
def reverse_print(texts):
    for text in texts:
        print(text[-1::-1], end = " ")
    print()
        
for _ in range(int(input())):
    reverse_print(input().split())