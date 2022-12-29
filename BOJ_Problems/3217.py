import sys
input = lambda : sys.stdin.readline().rstrip()
ALLOCATION_NUMBER = 1

def myPrint(var_name):
    target = namespace[var_name]
    if target == 0: print(0) # free된 메모리 공간
    else: print(target[0]) # 할당된 메모리 공간
    
def free(var_name):
    target = namespace[var_name]
    if target != 0: # 메모리가 할당된 상태면
        malloc_start_index, size = target
        for idx in range(size):
            memory[malloc_start_index + idx] = 0 # 할당된 메모리 공간의 각 셀을 비활성화

    namespace[var_name] = 0 # 메모리 해제 처리

def malloc(memory, size):
    try:
        malloc_start_index = 0 # 할당 성공시 할당된 공간의 첫 셀
        while True:
            if memory[malloc_start_index] == 0: # 미사용중인 셀 발견시 size만큼 '연속적으로' 할당 가능한지 확인
                temp_start = temp_end = malloc_start_index
                
                is_available_memory = True
                for _ in range(size):
                    if memory[temp_end] != 0:
                        is_available_memory = False
                        malloc_start_index = temp_end + 1
                        break
                    else:
                        temp_end += 1
                
                if is_available_memory:
                    for idx in range(size):
                        memory[temp_start + idx] = ALLOCATION_NUMBER
                    return [temp_start, size]
            else:
                malloc_start_index += 1
    except: # 10만개의 연속된 공간을 넘음(공간 부족)
        return 0



namespace, memory = {}, [None] + [0] * 100000 # 변수공간, 메모리

for _ in range(int(input())):
    line = input().split('=')
    var_name = line[0][line[0].index('(') + 1 : line[0].index(')')] if len(line) == 1 else line[0]
    
    if len(line) == 1: # print or free
        if line[0].startswith('p'): myPrint(var_name) # print
        else: free(var_name) # free
    else: # malloc
        size = int(line[1][line[1].index('(') + 1 : line[1].index(')')]) # malloc size
        namespace[var_name] = malloc(memory, size) # 할당 후 첫 셀을 변수공간에 담아줌