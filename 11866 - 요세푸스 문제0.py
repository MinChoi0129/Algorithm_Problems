n, k = map(int, input().split())

people = [j for j in range(1, n + 1)]

index = k - 1

popped = []

while len(people) > 1:
    popped.append(people.pop(index))
    index += k - 1
    while index >= len(people):
        index -= len(people)
popped.append(people[0])
        
print("<", end = "")
for i in range(len(popped)):
    if i <= len(popped) - 2:
        print(popped[i], end = ", ")
    else:
        print(popped[i], end = "")
print(">", end = "")