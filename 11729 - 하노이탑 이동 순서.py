def move(n, start, arrive):
    
    l = [1, 2, 3]
    l.remove(start)
    l.remove(arrive)
    temp = l[0]

    if n == 1:
        print("%d %d" %(start, arrive))

    else:
        move(n - 1, start, temp)
        move(1, start, arrive)
        move(n - 1, temp, arrive)


n = int(input())
print((2 ** n) - 1)
move(n, 1, 3)