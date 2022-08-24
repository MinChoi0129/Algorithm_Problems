def palindrom(get_s):
    length = len(get_s)
    check = "yes"
    for i in range(length // 2):
        if get_s[i] != get_s[(length - 1) - i]:
            check = "no"
            break
    return check

while True:
    get_s = input()
    
    if get_s == "0":
        break
    else:
        print(palindrom(get_s))