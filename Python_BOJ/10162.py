t = int(input())
a, b, c = 300, 60, 10
a_times, b_times, c_times = 0, 0, 0
count = 0
if t >= a:
    a_times = t // a
    t -= a_times * a

if t >= b:
    b_times = t // b
    t -= b_times * b

if t >= c:
    c_times = t // c
    t -= c_times * c

print(-1) if t > 0 else print(a_times, b_times, c_times)