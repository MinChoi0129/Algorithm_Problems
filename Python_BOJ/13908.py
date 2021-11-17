from itertools import product as PI, repeat
n, m = map(int, input().split())

if m != 0:
    must_in = set(input().split())
    must_in_len = len(must_in)

    count = 0
    for numbers in PI("0123456789", repeat = n):
        if len(must_in & set(numbers)) == must_in_len: 
            count += 1
        
    print(count)

else:
    print(10 ** n)