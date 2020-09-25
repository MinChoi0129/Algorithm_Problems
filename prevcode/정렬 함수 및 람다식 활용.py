import sys
n = int(sys.stdin.readline())

mem = []
for i in range(n):
    age, name = sys.stdin.readline().split()
    mem.append([age, name, i])

mem = sorted(mem, key = lambda x : int(x[0]))

for i in range(n):
    print(mem[i][0], mem[i][1])

################################################################################

sorted() : 모든 iterable 데이터에 대해 사용가능하며 return [list] (원본을 복사해와서 새로운 리스트를 반환하기때문에 원본은 훼손x)
vs
~~~.sort() : [list] 데이터에만 사용가능하며 return None (대신 원본 자체를 변경함)

################################################################################

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
