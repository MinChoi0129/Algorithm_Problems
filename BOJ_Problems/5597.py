bad_students = dict()
for i in range(1, 31):
    bad_students[i] = False
for i in range(28):
    bad_students[int(input())] = True

for key, value in bad_students.items():
    if not value: print(key)