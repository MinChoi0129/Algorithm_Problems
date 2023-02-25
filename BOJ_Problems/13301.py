n,a,b,c,d=int(input()),0,1,1,2
for _ in range(n-3):a,b,c,d=b,c,d,c+d
print(4 if n==1 else 6 if n==2 else 6*a+10*b)