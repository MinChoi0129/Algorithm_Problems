n,p=int(input()),10007
print((n if n<5 else pow(3,n//3)if n%3==0 else pow(3,(n-4)//3)*4 if n%3==1 else pow(3,(n-2)//3)*2)%p)