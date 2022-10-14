# class Matrix:
#     def __init__(self, matrix_data):
#         self.matrix = matrix_data
#         self.base_matrix = matrix_data
#     def __pow__(self, k):
#         if k == 1: return Matrix(self.base_matrix)
#         c = self ** (k//2)
#         return c * c if k % 2 == 0 else self * c * c
    
#     def __mul__(self, other):
#         if len(other.matrix[0]) == 2:
#             a, b, c, d, e, f, g, h = \
#                 self.matrix[0][0], self.matrix[0][1], self.matrix[1][0], self.matrix[1][1], \
#                 other.matrix[0][0], other.matrix[0][1], other.matrix[1][0], other.matrix[1][1]
#             return Matrix([[a*e+b*g, a*f+b*h], [c*e+d*g, c*f+d*h]])
#         elif len(other.matrix[0]) == 1:
#             a, b, c, d, e, f = \
#                 self.matrix[0][0], self.matrix[0][1], self.matrix[1][0], self.matrix[1][1], \
#                 other.matrix[0][0], other.matrix[1][0]
#             return Matrix([[a*e+b*f], [c*e+d*f]])

# x, y, a0, a1, n = map(int, input().split())

# p = Matrix([[x, y], [0, 1]]) ** (n-1)
# print(p.matrix[0][0] * a1 + p.matrix[0][1] * a0)