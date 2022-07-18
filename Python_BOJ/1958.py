from itertools import combinations as C
from sys import exit

texts = sorted([input(), input(), input()], key=lambda x:len(x))
standard_text = texts[0]
for length in range(len(standard_text), 0, -1):
    for item in C(standard_text, length):
        comparison_text = ''.join(item)
        if comparison_text in texts[1] and comparison_text in texts[2]:
            print(length)
            exit(0)