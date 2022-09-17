n = int(input())
matrix = [[1, 1], [1, 0]]
class SquareMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = 2
    def __pow__(self, other):
        pass
    def getValue(self):
        t = self.matrix
        return t[0][0]*t[1][1]-t[0][1]*t[1][0]