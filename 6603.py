from itertools import combinations as C
while True:
    getline =  input()
    if getline == '0':
        break
    
    k, *arr = map(int, getline.split())
    for case in C(arr, 6):
        for num in case:
            print(num, end = " ")
        print()
    print()