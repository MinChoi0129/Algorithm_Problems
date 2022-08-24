import sys

n = int(sys.stdin.readline().rstrip())

orders = []
stack = []
print_box = []
work_well = True

for _ in range(n):
    orders.append(int(sys.stdin.readline().rstrip()))

start = 1
for order in orders:
    while start <= order:
        stack.append(start)
        start += 1
        print_box.append('+')
    if stack[-1] == order:
        print_box.append('-')
        stack.pop()
    else:
        work_well = False
        break

if work_well:
    for i in print_box:
        print(i)
else:
    print("NO")