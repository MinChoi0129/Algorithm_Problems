def s(num):
    chosen_idx = None
    for i in range(len(arr)):
        if 2 ** i - 1 <= num <= 2 ** (i+1) - 1:
            if num == 2 ** (i+1) - 1:
                chosen_idx = i
            else:
                chosen_idx = i-1
            break
    
    l_d = num - (2 ** (chosen_idx - 1))
    r_d = (2 ** (chosen_idx + 1) - 1) - num

    if l_d <= r_d:
        result = arr[chosen_idx]
        for i in range(arr[chosen_idx] + 1, num + 1):
            result += bin(i).count('1')
    else:
        result = arr[chosen_idx + 1]
        for i in range(num + 1, arr[chosen_idx + 1] + 1):
            result -= bin(i).count('1')

    return result

    

a, b = map(int, input().split())

n = 1
arr = [0]
while n*n <=b:
    arr.append(arr[n-1] * 2 + 2 ** (n - 1))
    n += 1

print(s(b) - s(a-1))