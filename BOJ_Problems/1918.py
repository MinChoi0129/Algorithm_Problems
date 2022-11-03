def printer(e): print(e, end="")

stack = []
for e in list(input()):
    if e not in '()+-*/': printer(e)
    elif e == '(': stack.append(e)
    elif e == ')':
        while stack and stack[-1] != '(': printer(stack.pop())
        stack.pop()
    elif e in '*/':
        while stack and stack[-1] in '*/': printer(stack.pop())
        stack.append(e)
    else: # e in '+-'
        while stack and stack[-1] in '*/': printer(stack.pop())
        if stack and stack[-1] in '+-': printer(stack.pop())
        stack.append(e)
while stack: printer(stack.pop())