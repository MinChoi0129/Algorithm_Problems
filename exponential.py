from math import factorial

n = int(input())
e = 0.0
for depth in range(n):
    e += 1 / factorial(depth)
    
print("%.50f" % (e))
print(len("71828182845904553488480814849026501178741455078125"))