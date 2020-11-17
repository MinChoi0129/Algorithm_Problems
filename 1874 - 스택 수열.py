# pypy는 되고 python3는 안됨

import sys

n = int(sys.stdin.readline().rstrip())

num_box = [i for i in range(n, 0, -1)] # n, n-1, n-2, ..., 3, 2, 1
orders = [] # 만들고자 하는 수열 'order들'
stack = [] # 스택
print_box = [] # 출력 할 내용 담기
work_well = True # 수열 제작 가능성

for _ in range(n):
    orders.append(int(sys.stdin.readline().rstrip()))
    
for order in orders:
    while order not in stack: # 뽑고 싶은 수가 담길 때까지
        print_box.append('+') # push 명령 담기
        stack.append(num_box.pop()) # 1부터 차근차근 담기(썼던 숫자는 재사용 불가)
        
    # 올바른 'order' 인지 판단
    if stack[-1] == order:
        print_box.append('-') # pop 명령 담기
        stack.pop()
    else:
        work_well = False # 올바르지 않은 수열 'order'
        break

if work_well: # 옳은 수열이면 print_box에서 + - 출력
    for i in print_box:
        print(i)
else:
    print("NO")
    
"""
Fine = True
orders = 43687521
get_ready = (n to 1)

+ : stack.append(get_ready.pop())
-  : print(-) and stack.pop() (그 수가 맞을때만(stack[-1] == order). 아니면 멈추고 NO출력)

<시작>

For 4 :
++++ (while 4 not in stack) 
-

For 3 :
do nothing (while 3 not in stack)
-

For 6:
++ (while 6 not in stack)
-

…

"""