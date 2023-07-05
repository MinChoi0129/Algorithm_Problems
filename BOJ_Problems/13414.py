# from collections import OrderedDict


server = dict()

k, l = map(int, input().split())

for _ in range(l):
    student_id = input()
    if student_id not in server: server[student_id] = True
    else: server[student_id] = server.pop(student_id)

print(*[*server.keys()][:k], sep="\n")