def innerProduct(vec1, vec2, size, divisor): return (sum([(vec1[k] % divisor) * (vec2[k] % divisor) for k in range(size)])) % divisor

class Matrix:
    def __init__(self, array_2d):
        self.array = array_2d
    def __mul__(self, other):
        size, divisor = len(self.array), 1000
        other = Matrix([list(e) for e in zip(*other.array[::-1])])
        return Matrix([[innerProduct(self.array[i], other.array[j][::-1], size, divisor) for j in range(size)] for i in range(size)])
    def __pow__(self, exp):
        if exp == 1: return self
        elif exp % 2 == 0:
            conquer = self ** (exp // 2)
            return conquer * conquer
        else:
            conquer = self ** ((exp - 1) // 2)
            return self * conquer * conquer
    def __str__(self):
        txt = ""
        for line in self.array:
            for element in line: txt += str(element % 1000) + " "
            txt += "\n"
        return txt

N, B = map(int, input().split())
print((Matrix([[*map(int, input().split())] for _ in range(N)]) ** B))