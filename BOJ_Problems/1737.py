from sys import setrecursionlimit as SRL
SRL(100000000)
pi = 3.1
fibos = dict()
def fibo(num):
    if num in fibos:
        return fibo(num)
    else:
        if 0 <= num <= pi:
            fibos[num] = 1

    fibos[num] = (fibo(num - 1) + fibo(num - pi))
    return fibos[num]

print(fibo(int(input())) % (10 ** 18))