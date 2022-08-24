A, B = input().split()

tot_A, tot_B = 0, 0
for a in A:
    tot_A += int(a)
for b in B:
    tot_B += int(b)

print(tot_A * tot_B)