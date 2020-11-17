import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    count = 0
    n, m = map(int, sys.stdin.readline().rstrip().split())
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    printer = []
    for i in range(len(temp)):
        printer.append((temp[i], i))
    
    while len(printer) > 0:
        if printer[0][0] == max(printer)[0]:
            result = printer.pop(0)[1]
            count += 1
            if result == m:
                break
        else:
            printer.append(printer.pop(0))
    print(count)