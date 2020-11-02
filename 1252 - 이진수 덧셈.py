def bin_to_dec(num):
    new_num_0 = []
    new_num_1 = []
    for i in num[0]:
        new_num_0.append(int(i))
    for i in num[1]:
        new_num_1.append(int(i))
        
    while len(new_num_0) > 0 and new_num_0[0] == 0:
        new_num_0.pop(0)
    while len(new_num_1) > 0 and new_num_1[0] == 0:
        new_num_1.pop(0)
        
    len_0 = len(new_num_0)
    len_1 = len(new_num_1)
    sum_0 = 0
    sum_1 = 0
    for i in range(len_0):
        sum_0 += new_num_0[i] * (2 ** (len_0 - 1 - i))
                                   
    for i in range(len_1):
        sum_1 += new_num_1[i] * (2 ** (len_1 - 1 - i))
                        
    return [sum_0, sum_1] 
    
def print_dec_to_bin(num):
    if num == 0:
        print(0)
        return
    storage = []
    while num // 2 >= 2:
        storage.append(num % 2)
        num = num // 2
        
    storage.append(num % 2)
    storage.append(num // 2)
    storage.reverse()
    for i in storage:
        print(i, end = "")

a = bin_to_dec(list(input().split()))
print_dec_to_bin(a[0] + a[1])