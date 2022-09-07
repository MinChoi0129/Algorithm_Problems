a=lambda:input().split()
k=int(a()[1])
print(sorted(map(int,a()))[-k])