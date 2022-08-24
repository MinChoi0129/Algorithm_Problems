N, K = int(input()), int(input())
start, end = 1, K

while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for i in range(1, N+1) :
        tmp += min(mid // i, N)
        '''
        min 하는 이유 :
        한 행당 최대 N개까지 원소가 있을 수 있는데,
        (mid / i == 한 행당 조건을 만족하는 최대 원소 개수) > N 이면 안되기 때문이다.
        '''
    if tmp >= K:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1
print(ans)


'''
m = 임의의 숫자
이 임의의 m이 K번째 수 인지 판단해보자.

i행의 숫자들은 i*1, i*2, i*3, ..., i*N (board size = N by N)으로 구성되어 있다.

i행의 숫자들 중 m보다 작거나 같은 숫자는 (i*j <= m)를 만족하는 "j의 개수"이고

이는 i*1, i*2, ..., i*j이므로, j = m // i 이다.(왜냐하면 i*j=m -> j=m//i)
'''