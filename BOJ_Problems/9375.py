def fashion():
    get = 1
    n = int(input())
    if n == 0:
        print("0")
    
    else:
        cloth = dict()
        for i in range(n):
            c_name, c_type = map(str, input().split())
            if c_type in cloth.keys():
                cloth[c_type] = cloth[c_type] + 1
            else:
                cloth[c_type] = 1

        for i in cloth.keys():
            cloth[i] = cloth[i] + 1

            
        for i in cloth.keys():
            get = get * cloth[i]
        print("%d" % (get-1))
           
n = int(input())
for i in range(n):
    fashion()
