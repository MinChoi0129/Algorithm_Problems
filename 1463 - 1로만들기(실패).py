def one(x):
    count = 0
    while x != 1:
        while x % 3 == 0:
            x /= 3
            count += 1
        if x == 1:
            break
        if x - 2 == 1:
            count += 1
            break
        if x - 1 == 1:
            count += 1
            break
            
        if (x - 1) % 3 == 0 or (x - 2) % 3 == 0:
            if (x - 1) % 3 == 0:
                x -= 1
                count += 1
            else:
                x -= 2
                count += 1
    
    print(count)

one(int(input()))