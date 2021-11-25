import sys
input = lambda : sys.stdin.readline().rstrip()

def getTranslatableCount(word):
    word = list(word)
    first_end = word[0] + word[-1]
    middle_word = ''.join(sorted(word[1:-1]))
    return dictionary[first_end + middle_word]

n = int(input())
dictionary = dict()

for _ in range(n):
    word = list(input())
    key = ""
    if len(word) <= 2:
        key = word
    else:        
        first_end = word[0] + word[-1]
        middle_word = ''.join(sorted(word[1:-1]))
        key = first_end + middle_word
    
    if key not in dictionary: dictionary[key] = 1
    else: dictionary[key] += 1
        
for _ in range(int(input())):
    if n == 0:
        print(0)
    else:
        sentence = input().split()
        result = 1
        for word in sentence:
            if len(word) <= 2:
                result *= 1
            else:
                result *= getTranslatableCount(word)
        print(result)
