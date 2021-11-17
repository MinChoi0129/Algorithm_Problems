num = []

for i in range(9):
    num.append(int(input()))

maximum = num[0]
index = 0


print(max(num))
print(num.index(max(num)))