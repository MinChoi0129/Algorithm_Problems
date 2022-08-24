data = list(input())

stack = []

result = 0
for i in range(len(data)):
    if data[i] == '(': 
        stack.append(data[i])

    else: # ')
        if data[i-1] == '(': # 열자마자 닫기
            stack.pop()
            result += len(stack)
        else: # 닫고 닫히기
            stack.pop()
            result += 1
            
print(result)