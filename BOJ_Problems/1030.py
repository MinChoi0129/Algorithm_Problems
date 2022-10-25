for num in range(int(input()), 0, -1):
    if not (set(str(num)) & set("01235689")):
        print(num)
        break