import sys

def balanced(talk):

    stack = []
    
    for i in talk:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0 or stack[-1] == "[":
                return "no"
            else:
                stack.pop()
        elif i == "[":
            stack.append(i)
        elif i == "]":
            if len(stack) == 0 or stack[-1] == "(":
                return "no"
            else:
                stack.pop()
    if len(stack) > 0:
        return "no"            
    return "yes"
    

brackets = ['(', ')', '[', ']']

sentences = []

while True:
    sentence = list(sys.stdin.readline().rstrip())
    if len(sentence) == 1 and sentence[0] == ".":
        break
    else:
        temp = []
        for i in sentence:
            if i in brackets:
                temp.append(i)
        sentences.append(temp)
    
for sentence in sentences:
    print(balanced(sentence))