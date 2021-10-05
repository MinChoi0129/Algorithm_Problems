def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a, b = bin(arr1[i])[2:], bin(arr2[i])[2:]
        a = '0' * (n - len(a)) + a
        b = '0' * (n - len(b)) + b
        tmp = ""
        for j in range(n):
            result = int(a[j]) | int(b[j])
            tmp += ('#' if result == 1 else ' ')
        answer.append(tmp)
    return answer