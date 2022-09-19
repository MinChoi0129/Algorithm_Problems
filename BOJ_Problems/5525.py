n, m, s = int(input()), int(input()), input()
p = 'I' + 'OI' * n
count = 0
for move in range(m - (2*n + 1)):
    if p == s[move:move+2*n + 1]:
        count += 1
print(count)