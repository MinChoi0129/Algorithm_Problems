def fact(num,p):
    result=1
    for i in range(2,num+1):result=(result*i)%p
    return result
def power(b,e,p):
    if e==0:return 1
    if e%2==0:return(power(b,e//2,p)**2)%p
    else:return(b*(power(b,(e-1)//2,p)**2))%p
n,k,p=*map(int,input().split()),1000000007
print((fact(n,p)*power(fact(n-k,p)*fact(k,p),p-2,p))%p)