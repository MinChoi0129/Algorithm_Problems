data = input()

count, answer = 0, int(data) % 3 == 0
while data not in "369" and len(data) >= 2:
    data = str(sum(map(int, data)))
    count += 1

print(count)
print("YES" if answer else "NO")