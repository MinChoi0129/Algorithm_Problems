class DoubleLinkedList:
    def __init__(self, left, item, right):
        self.left = left
        self.item = item
        self.right = right
        self.used = False

def malloc(var_name, head, size):
    try:
        return_head = head
        while True:
            if return_head.used == False:
                trying_head = return_head
                trying_tail = trying_head
                is_usable = True
                for _ in range(size):
                    if trying_head.used == True:
                        is_usable = False
                        break
                    else:
                        trying_tail = trying_tail.right
                
                if is_usable:
                    while trying_head != trying_tail:
                        trying_head.used = True
                        trying_head = trying_head.right
                    return [return_head, size]
                else:
                    return_head = return_head.right
            else:
                return_head = return_head.right
    except:
        return 0

def myPrint(var_name):
    target = variables[var_name]
    if target == 0: print(0)
    else: print(target[0].item)
    
def free(var_name):
    target = variables[var_name]
    if target != 0:
        head, size = target
        for _ in range(size):
            head.used = False
            head = head.right
    variables[var_name] = 0

def initiateDoubleLinkedList():
    head, tail = None, None
    for i in range(1, 100001):
        if head is None:
            new_node = DoubleLinkedList(None, i, None)
            head = new_node
            tail = new_node
        else:
            new_node = DoubleLinkedList(tail, i, None)
            tail.right = new_node
            tail = new_node
    return head, tail

head, tail = initiateDoubleLinkedList()

variables = {} # 변수 공간 namespace
for _ in range(int(input())):
    line = input().split('=')
    if len(line) == 1: # print or free
        var_name = line[0][line[0].index('(') + 1 : line[0].index(')')]
        target = variables[var_name]
        if line[0].startswith('p'): myPrint(var_name)
        else: free(var_name)
    else: # malloc
        size = int(line[1][line[1].index('(') + 1 : line[1].index(')')])
        variables[line[0]] = malloc(line[0], head, size)