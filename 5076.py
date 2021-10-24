def check(string):
    stack, inTag, word = [], False, ""
    for i in range(len(string)): 
        if string[i] == '<': inTag = True        
        elif string[i] == '>': 
            inTag = False
            if word and word[-1] == '/':
                word = ''
                continue
            elif stack and stack[-1] == word[1:]: stack.pop()
            else: stack.append(word)
            word = ''
        if inTag and string[i] == ' ' and string[i + 1] != '/': inTag = False
        if inTag and string[i] != '<': word += string[i]
    return False if stack else True
while True:
    string = input()
    if string == '#': break
    else: print("legal" if check(string) else "illegal")