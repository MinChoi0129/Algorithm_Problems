def counting(n, k):
    count = 0
    while n != 1:
        if n % k == 0:
            n /= k
            count += 1
        else:
            n -= 1
            count += 1
    return count

n, k = map(int, input().split())
print(counting(n, k))