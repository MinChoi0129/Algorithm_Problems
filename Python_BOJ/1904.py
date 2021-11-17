import sys

def fill_fibo_list(n):
    for i in range(2, n):
        fibo_list.append((fibo_list[i - 1] % 15746 + fibo_list[i - 2] % 15746) % 15746)
        
fibo_list = [1, 2]

n = int(sys.stdin.readline().rstrip())
fill_fibo_list(n)
print(fibo_list[n - 1])