def calculate(a, b, op):
    try: a = value[a]
    except: pass

    try: b = value[b]
    except: pass

    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b
    elif op == '/': return a / b

n = int(input())
statement = list(input())
value = { chr(65 + i): int(input()) for i in range(n) }

stack = []

for element in statement:
    if element in '+-*/':
        a, b = stack.pop(), stack.pop()
        stack.append(calculate(b, a, element))
    else:
        stack.append(element)

print("%.2f" % stack[0])