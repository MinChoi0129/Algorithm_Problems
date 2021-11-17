n, k = map(int, input().split())

numbers = [*range(1, n + 1)]

print("<", end = "")
idx = k - 1
while numbers:
    try:
        if len(numbers) != 1:
            print(numbers.pop(idx), end = ", ")
        else:
            print(numbers.pop(idx), end = "")
        idx += k - 1
    except:
        idx -= len(numbers)
print(">")