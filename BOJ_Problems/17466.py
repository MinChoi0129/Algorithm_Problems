n,p=map(int,input().split());fact=1
for i in range(1,n+1):fact=(fact*i)%p
print(fact%p)