x, y = map(int, input().split())

z = (100 * y) // x

if z >= 99:
    print(-1)

else:
    start, end = 1, 1000000000
    result = 0
    while start <= end:
        mid = (start + end) // 2
        
        new_z = 100 * (y + mid) // (x + mid)
        
        if new_z <= z:
            start = mid + 1
        else:
            end = mid - 1
            result = mid
    print(result)