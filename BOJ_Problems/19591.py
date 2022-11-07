from collections import deque

def getDividedStatementDeque() -> deque:
    statement = deque()
    current_string = ""

    for e in input():
        if e in '0123456789':
            current_string += e
        else:
            if current_string:
                statement.append(current_string)
                current_string = ""
            statement.append(e)
    if current_string: statement.append(current_string)

    if statement[0] == '-':
        pop = statement.popleft()
        statement[0] = pop + statement[0]

    for i in range(len(statement)):
        try: statement[i] = int(statement[i])
        except: continue

    return statement

def priority(op): return 1 if op in '*/' else 0

statement = getDividedStatementDeque()

while '*' in statement or '/' in statement or '+' in statement or '-' in statement:
    left, right = [], []
    for i in range(3): left.append(statement[i])
    for i in range(3): right.append(statement[len(statement)-1-i])

    p_left, p_right = priority(left[1]), priority(right[1])
    if p_left == p_right: # 우선순위 같음
        if left[1] == '*': calc_left = left[0] * left[2]
        elif left[1] == '/':
            if left[0] * left[2] < 0: calc_left = left[0] // left[2] + 1
            else: calc_left = left[0] // left[2]
        elif left[1] == '+': calc_left = left[0] + left[2]
        elif left[1] == '-': calc_left = left[0] - left[2]

        if right[1] == '*': calc_right = right[2] * right[0]
        elif right[1] == '/':
            if right[0] * right[2] < 0: calc_right = right[2] // right[0] + 1
            else: calc_right = right[2] // right[0]
        elif right[1] == '+': calc_right = right[2] + right[0]
        elif right[1] == '-': calc_right = right[2] - right[0]
        
        if calc_left >= calc_right:
            for i in range(3): statement.popleft()
            statement.appendleft(calc_left)
        else:
            for i in range(3): statement.pop()
            statement.append(calc_right)
    elif p_left > p_right:
        if left[1] == '*':
            calc_left = left[0] * left[2]
        elif left[1] == '/':
            if left[0] * left[2] < 0: calc_left = left[0] // left[2] + 1
            else: calc_left = left[0] // left[2]
        elif left[1] == '+':
            calc_left = left[0] + left[2]
        elif left[1] == '-':
            calc_left = left[0] - left[2]
        for i in range(3): statement.popleft()
        statement.appendleft(calc_left)
    elif p_left < p_right:
        if right[1] == '*':
            calc_right = right[2] * right[0]
        elif right[1] == '/':
            if right[0] * right[2] < 0: calc_right = right[2] // right[0] + 1
            else: calc_right = right[2] // right[0]
        elif right[1] == '+':
            calc_right = right[2] + right[0]
        elif right[1] == '-':
            calc_right = right[2] - right[0]
        for i in range(3): statement.pop()
        statement.append(calc_right)

print(statement[0])