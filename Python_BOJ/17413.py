letter = input()
splitted = []

idx = 0
while True:
    tmp = ""
    try:
        if letter[idx] == "<":
            while True:
                if letter[idx] != ">":
                    tmp += letter[idx]
                    idx += 1
                else:
                    tmp += letter[idx]
                    idx += 1
                    splitted.append(tmp)
                    tmp = ""
                    break
            
        else:
            while True:
                if letter[idx] != "<":
                    tmp += letter[idx]
                    idx += 1
                else:
                    splitted.append(tmp)
                    tmp = ""
                    break
    except:
        splitted.append(tmp)
        break
            
for i in splitted:
    if "<" in i:
        print(i, end = "")
    else:
        tmp = i.split()
        for j in range(len(tmp)): # j = 0, 1
            for k in reversed(tmp[j]): # k = problem, ever
                print(k, end = "")
            if j != len(tmp) - 1:
                print(" ", end = "")
print()