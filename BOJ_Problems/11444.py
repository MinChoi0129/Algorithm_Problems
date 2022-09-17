class Matrix:
    def __init__(self, matrix): self.matrix = matrix
    def __str__(self): return str(self.matrix[0][1])    
    def __mul__(self, other):
        x, y = self.matrix, other.matrix
        a, b, c, d, e, f, g, h = x[0][0], x[0][1], x[1][0], x[1][1], y[0][0], y[0][1], y[1][0], y[1][1]
        return Matrix([[(a*e+b*g) % p, (a*f+b*h) % p], [(c*e+d*g) % p, (c*f+d*h) % p]])
    def __pow__(self, n):
        if n == 1: return self
        c = self ** (n//2)
        if not n % 2: return c*c
        else: return c*c*self
    
n, p = int(input()), 1000000007
if not n: print(0)
else: print(Matrix([[1, 1], [1, 0]]) ** n)