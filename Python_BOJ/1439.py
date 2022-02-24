string = input()
count = [0, 0]

for char in string.split('0'):
    if char != "": count[0] += 1

for char in string.split('1'):
    if char != "": count[1] += 1

print(min(count))