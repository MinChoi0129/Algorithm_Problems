'''
ㄱ. 새 건물의 높이(y)가 커지면 +1
ㄴ. 새 건물의 높이(y)가 작아지면 스택의 마지막 값(stack[-1])이 '본인 이하'(<=y)가 될때까지 삭제
    (삭제 과정에서 미만(<)이 된 경우 자신을 추가하여 이하(등호 추가)로 유지.)
ㄷ. 잔여 스택은 무시 가능.(입력을 받자마자 처리하였기 때문. (스택관리 우선하지않고 증감에 따른 append pop에 우선함.))
'''

stack, count = [0], 0
for _ in range(int(input())):
    y = int(input().split()[1])
    
    # Part 1
    if stack and y > stack[-1]:
        count += 1
        stack.append(y)
    else:
        # Part 2 
        while stack and y < stack[-1]:
            stack.pop()
            
        # Part 1
        if stack and y > stack[-1]:
            count += 1
            stack.append(y)
            
print(count)