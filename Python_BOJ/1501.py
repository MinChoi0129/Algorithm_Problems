import sys
input = lambda : sys.stdin.readline().rstrip()

def getTranslatableCount(word : str):
    if len(word) <= 2:
        try: return dictionary[word]
        except: return 0
    else:
        first_end = word[0] + word[-1]
        middle_word = ''.join(sorted(word[1:-1]))
        try: return dictionary[first_end + middle_word]
        except: return 0

# 사전 만들기
dictionary = dict()
for _ in range(int(input())):
    word = input()
    key = ""
    if len(word) <= 2:
        key = word
    else:
        first_end = word[0] + word[-1]
        middle_word = ''.join(sorted(word[1:-1]))
        key = first_end + middle_word
    
    if key not in dictionary: dictionary[key] = 1
    else: dictionary[key] += 1
        
# 문장 해석
for _ in range(int(input())):
    sentence = input().split()
    result, possible = 1, False
    
    for word in sentence:
        val = getTranslatableCount(word)
        if val != 0:
            result *= val; possible = True
                   
    print(result if possible else 0)