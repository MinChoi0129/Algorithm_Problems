a,b=0,1
for _ in range(((int(input()))%(15*10**5))-1):a,b=b,(a+b)%1000000
print(b)