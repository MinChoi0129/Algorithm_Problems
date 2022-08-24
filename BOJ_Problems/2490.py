def chk(yuts):
    bae_count = 0
    for yut in yuts:
        if yut == "0":
            bae_count += 1
    if bae_count == 0:
        return "E"
    elif bae_count == 1:
        return "A"
    elif bae_count == 2:
        return "B"
    elif bae_count == 3:
        return "C"
    elif bae_count == 4:
        return "D"
    

for _ in range(3):
    print(chk(input().split()))