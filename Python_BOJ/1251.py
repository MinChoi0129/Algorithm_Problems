from itertools import combinations as C
word = input()
words = [word[:p1][::-1] + word[p1:p2][::-1] + word[p2:][::-1] for p1, p2 in C(range(1, len(word)), 2)]
print(sorted(words)[0])