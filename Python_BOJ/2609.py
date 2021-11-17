def is_prime(num):  # 소수 판별
    for i in range(2, num):  # 2부터 자기자신-1 까지 나눠지는지 확인
        if num % i == 0:
            return False
    return True


def make_prime_list(small):  # 소수 리스트 제작 함수
    global primes
    for i in range(2, small + 1):  # 나눌 수(==소수들) 리스트 만들기, 작은 수(포함)까지만
        if is_prime(i):
            primes.append(i)


def gcd(big, small):  # 최대공약수 영어로 greatest common denominator
    global primes
    value = 1
    for i in primes:
        while big % i == 0 and small % i == 0:
            value *= i
            big /= i
            small /= i
    return value


def lcm(big, small, gcd):  # 최소공배수 영어로 least common multiple
    mul_1 = big // gcd
    mul_2 = small // gcd
    return gcd * mul_1 * mul_2


#################################################################################################
arr = list(map(int, input().split()))  # 숫자 두 개 받아서
big = max(arr)  # 큰 수
small = min(arr)  # 작은 수로 구분하고

primes = []  # 소수담을 칸 만든다음
make_prime_list(small)  # 작은 수 이하까지 소수 담고

gcd = gcd(big, small)  # 최대공약수
lcm = lcm(big, small, gcd)  # 최소공배수를 최대공약수를 통해 구하기

print(gcd)
print(lcm)