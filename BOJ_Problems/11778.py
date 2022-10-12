class Matrix:
    def __init__(self, matrix_array):
        self.matrix = matrix_array
        self.base_matrix = matrix_array
    
    def __mul__(self, other):
        a, b, c, d = self.matrix[0][0], self.matrix[0][1], self.matrix[1][0], self.matrix[1][1]
        e, f, g, h = other.matrix[0][0], other.matrix[0][1], other.matrix[1][0], other.matrix[1][1]
        return Matrix([\
            [   ((a*e) % P + (b*g) % P) % P,    ((a*f) % P + (b*h) % P) % P     ],
            [   ((c*e) % P + (d*g) % P) % P,    ((c*f) % P + (d*h) % P) % P     ]
        ])
    def __pow__(self, k):
        if k == 1: return Matrix(self.base_matrix)
        c = self ** (k//2)
        return c * c if k % 2 == 0 else self * c * c

import math
n, m, P = *map(int, input().split()), 1000000007
print((Matrix([[1, 1], [1, 0]]) ** math.gcd(n, m)).matrix[0][1])