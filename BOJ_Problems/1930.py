for _ in range(int(input())):
    a,b,c,d,e,f,g,h = map(int,input().split())

    t = {
        (a,(b,c,d)),(a,(c,d,b)),(a,(d,b,c)),
        (b,(c,a,d)),(b,(a,d,c)),(b,(d,c,a)),
        (c,(d,a,b)),(c,(a,b,d)),(c,(b,d,a)),
        (d,(a,c,b)),(d,(c,b,a)),(d,(b,a,c))}

    print(1 if (e,(f,g,h)) in t else 0)