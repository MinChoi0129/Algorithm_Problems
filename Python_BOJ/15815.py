statement, stack = input(), []
for i in statement:
    try:
        int(i)
        stack.append(i)
    except:
        a = stack.pop()
        b = stack.pop()
        if i == '/' : stack.append(str(eval(b + "//" + a)))
        else: stack.append(str(eval(b + i + a)))
print(stack.pop())