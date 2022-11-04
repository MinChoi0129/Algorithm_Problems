from collections import deque

def isBracketPerfect(statement):
    stack = deque()
    for e in statement:
        if e == '(':
            stack.append(e)
        elif e == ')':
            if not stack or stack[-1] != '(': return False
            stack.pop()
    return True

statement = input()

if not isBracketPerfect(statement): print(0)
else:
    while '()' in statement:
        statement = statement.replace('()', '2')

    while '[]' in statement:
        statement = statement.replace('[]', '3')

    stack = deque()
    for e in statement:
        if e in '([':
           stack.append(e)
       
        elif e == ']':
            left_bracket, num = stack.pop(), int(stack.pop())
            new_num = 3 * num
            try:
                stack[-1]
                int(stack[-1])

                left = int(stack.pop())
                stack.append(str(left + new_num))
            except:
                stack.append(e)

            
        else:
            try:
                stack[-1]
                int(stack[-1])

                left = int(stack.pop())
                right = int(e)
                stack.append(str(left + right))
            except:
                stack.append(e)
            
