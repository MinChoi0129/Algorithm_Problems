from collections import deque

def getDividedStatementDeque() -> deque:
    statement = deque()
    current_string = ""
    opcount = 0
    for e in input():
        if e in '0123456789':
            current_string += e
        else:
            opcount += 1
            if current_string:
                statement.append(current_string)
                current_string = ""
            statement.append(e)
    if current_string: statement.append(current_string)

    if statement[0] == '-':
        opcount -= 1
        pop = statement.popleft()
        statement[0] = pop + statement[0]

    return statement, opcount

def priority(op):
    return 1 if op in '*/' else 0

def calculate(command):
    left, op, right = int(command[0]), command[1], int(command[2])
    if op == '+': return left + right
    elif op == '-': return left - right
    elif op == '*': return left * right
    elif left * right < 0: return left // right + 1
    else: return left // right

s, opcount = getDividedStatementDeque()

while opcount:
    left, right = [s[0], s[1], s[2]], [s[-3], s[-2], s[-1]]

    p_left, p_right = priority(left[1]), priority(right[1])
    calc_left, calc_right = calculate(left), calculate(right)

    if p_left == p_right: # 우선순위 같음
        if calc_left >= calc_right:
            for i in range(2): s.popleft()
            s[0] = calc_left
        else:
            for i in range(2): s.pop()
            s[-1] = calc_right
    elif p_left > p_right:
        for i in range(2): s.popleft()
        s[0] = calc_left
    else:
        for i in range(2): s.pop()
        s[-1] = calc_right
    opcount -= 1

print(int(s[0]))