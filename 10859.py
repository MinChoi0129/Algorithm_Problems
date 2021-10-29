def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0: return False
    return True

def getRotatedNum(string):
    tmp, turned = "", {'0':'0', '1':'1', '2':'2', '5':'5', '8':'8', '6':'9', '9':'6'}
    for txt in string: tmp += turned[txt]
    return int(''.join(tmp))

num = input()
if len(set(num) & set("347")) >= 1 or num == '1': print("no")
else: print("yes" if is_prime(getRotatedNum(''.join(reversed(num)))) else "no") if is_prime(int(num)) else print("no")