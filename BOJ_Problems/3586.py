import math

class Fraction:
    def __init__(self, p: int, q: int) -> None:
        self.p = p // math.gcd(p, q)
        self.q = q // math.gcd(p, q)
        if self.p == 0: self.q = 1

    def __add__(self, other: 'Fraction') -> 'Fraction':
        return Fraction(self.p * other.q + self.q * other.p, self.q * other.q)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        return self + Fraction(-other.p, other.q)

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        return Fraction(self.p * other.p, self.q * other.q)

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        return self * Fraction(other.q, other.p)

    def __eq__(self, other: 'Fraction') -> bool:
        left, right = Fraction(self.p, self.q), Fraction(other.p, other.q)
        return left.p == right.p and left.q == right.q

    def __str__(self) -> str:
        if self.q < 0:
            self.p *= -1
            self.q *= -1
        return str(self.p) + '/' + str(self.q)

class FractionalRationalNumber:
    def __init__(self, a, b, c, d) -> None:
        if type(a) == int:
            self.a = Fraction(a, 1)
            self.b = Fraction(b, 1)
            self.c = Fraction(c, 1)
            self.d = Fraction(d, 1)
        elif type(a) == Fraction:
            self.a = a
            self.b = b
            self.c = c
            self.d = d
    
    def __add__(self, other: 'FractionalRationalNumber') -> 'FractionalRationalNumber':
        a, b, c, d = self.a, self.b, self.c, self.d
        e, f, g, h = other.a, other.b, other.c, other.d
        return FractionalRationalNumber(a*h+b*g+c*f+d*e, b*h+d*f, c*h+d*g, d*h)

    def __sub__(self, other: 'FractionalRationalNumber') -> 'FractionalRationalNumber':
        other.a *= Fraction(-1, 1)
        other.b *= Fraction(-1, 1)
        return self + other

    def __mul__(self, other: 'FractionalRationalNumber') -> 'FractionalRationalNumber':
        a, b, c, d = self.a, self.b, self.c, self.d
        e, f, g, h = other.a, other.b, other.c, other.d
        return FractionalRationalNumber(a*f+b*e, b*f, c*h+d*g, d*h)

    def __truediv__(self, other: 'FractionalRationalNumber') -> 'FractionalRationalNumber':
        if other.a == Fraction(0, 1) and other.b == Fraction(0, 1):
            raise ZeroDivisionError()
        return self * FractionalRationalNumber(other.c, other.d, other.a, other.b)

def calculatePostFix(statement: list, *optional) -> FractionalRationalNumber:
    stack = []
    x_in = [Fraction(0, 1), optional[0], Fraction(0, 1), Fraction(1, 1)] if optional else [1, 0, 0, 1]
    for e in statement:
        if e in '+-*/':
            right = stack.pop(); left = stack.pop()
            if e == '+': stack.append(left + right)
            elif e == '-': stack.append(left - right)
            elif e == '*': stack.append(left * right)
            elif e == '/': stack.append(left / right)
        elif e == 'X': stack.append(FractionalRationalNumber(*x_in))
        else: stack.append(FractionalRationalNumber(0, int(e), 0, 1))
    return stack.pop()
    

def main(s: list):
    result = calculatePostFix(s)
    if result.a != Fraction(0, 1):
        x = Fraction(-result.b.p, result.a.p)
        try:
            calculatePostFix(s, x)
            print("X =", str(x))
        except:
            print("NONE")
    elif result.c != Fraction(0, 1):
        if result.d == Fraction(0, 1):
            print("MULTIPLE")
        else:
            print("NONE")
    elif result.d != Fraction(0, 1) and result.b == Fraction(0, 1):
        print("MULTIPLE")
    else:
        print("NONE")



# for tc in ["4 X * 2 + 2 /", "1 2 / 2 4 / - X *", "1 1 X 2 + / /"]:
#     main(tc.split())

main(input().split())