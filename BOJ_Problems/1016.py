small, big = map(int, input().split())
is_square_number = [False] * (big-small)
for num in range(2, big):
    chekcing_number = num ** 2
    if chekcing_number-small > big: break
    is_square_number[chekcing_number-small] = True
    for multiplier in range(2, big):
        multiplied_checking_number = chekcing_number * multiplier
        if multiplied_checking_number-small > big: break
        is_square_number[multiplied_checking_number-small] = True
print(is_square_number.count(False)-1)