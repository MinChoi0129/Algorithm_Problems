A, B = map(int, input().split()); i, count, stack = 1, 1, []
while len(stack) != B:
    while count <= i and len(stack) != B:
        stack.append(i)
        count += 1
    i += 1
    count = 1
print(sum(stack[A - 1 : B]))