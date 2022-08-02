import math;a,b,c=map(int,input().split());l,r,s=(c-b)/a,(c+b)/a,50000
while l<r and s:
    x=(l+r)/2
    if x<(c-b*math.sin(x))/a:l=x+0.000000001
    else:r=x
    s-=1
print(x)