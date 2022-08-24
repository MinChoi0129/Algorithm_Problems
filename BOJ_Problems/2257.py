mass_table, stack, chemical_statement = {'H':1, 'C':12, 'O':16}, [], input()

for char in chemical_statement:
    if char in mass_table: stack.append(mass_table[char]) # 원소기호
    elif char == '(': stack.append(char) # 개괄호
    elif char in "23456789": stack.append(stack.pop() * int(char)) # 숫자
    elif char == ')': # 폐괄호
        sum_in_bracket = 0
        while True:
            pop = stack.pop() # 5번줄과 연계, 정수형
            if pop == '(': break
            sum_in_bracket += pop
        stack.append(sum_in_bracket)
print(sum(stack))