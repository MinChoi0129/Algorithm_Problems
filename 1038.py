n = int(input())

descendingNumbers, count = [0,1,2,3,4,5,6,7,8,9], 10
is_descending = dict()

for i in range(10):
    is_descending[str(i)] = True
    
num = 10
while True:
    
    if num > 987654321 or count >= n + 1:
        break
    
    str_num = str(num)
    if int(str_num[0]) <= int(str_num[1]): # 첫 두자리수부터 감소 안함
        is_descending[str_num] = False
    else: # 첫 두자리수는 감소
        try:
            if not is_descending[str_num[1:]]:
                is_descending[str_num] = False
            else:
                is_descending[str_num] = True
                descendingNumbers.append(num)
                count += 1
        except:
            flag = True
            for i in range(len(str_num) - 1):
                if str_num[i] <= str_num[i+1]:
                    flag = False
                    break
            
            is_descending[str_num] = flag
            
            if flag:                
                descendingNumbers.append(num)
                count += 1

    num += 1
    
try: print(descendingNumbers[n])
except: print(-1)