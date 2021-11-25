dictionary = dict()
for _ in range(int(input())):
    word = list(input())
    add_target = ()
    if len(word) <= 2:
        add_target = (word, dict())
    else:        
        first_end = word[0] + word[-1]
        middle_word = word[1:-1]
        tmp = dict()
        for char in middle_word:
            if char not in tmp: tmp[char] = 1
            else: tmp[char] += 1
        add_target = (middle_word, tmp)
    
    if add_target not in dictionary: dictionary[add_target] = 1
    else: dictionary[add_target] += 1

print(dictionary)
        

for _ in range(int(input())):
    sentence = input().split()
    result = 1
    
