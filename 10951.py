while True:
    try:
        get = list(map(int, input().split()))
        print(get[0] + get[1])
    except:
        break