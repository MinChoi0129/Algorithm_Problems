import math

class BaseFraction:
    def __init__(self, p: int, q: int) -> None: self.p = p // math.gcd(p, q); self.q = q // math.gcd(p, q)    
    def __add__(self, other: 'BaseFraction') -> 'BaseFraction': return BaseFraction(self.p * other.q + self.q * other.p, self.q * other.q)
    def __sub__(self, other: 'BaseFraction') -> 'BaseFraction': return self + (-other)
    def __mul__(self, other: 'BaseFraction') -> 'BaseFraction': return BaseFraction(self.p * other.p, self.q * other.q)
    def __truediv__(self, other: 'BaseFraction') -> 'BaseFraction': return self * BaseFraction(other.q, other.p)
    def __eq__(self, other: 'BaseFraction') -> bool: return self.p == other.p and self.q == other.q
    def __neg__(self) -> 'BaseFraction': return BaseFraction(-self.p, self.q)
    def __str__(self) -> str: return str(self.p) + '/' + str(self.q) if self.q > 0 else str(-self.p) + '/' + str(-self.q)

class AdvancedFraction:
    def __init__(self, a, b, c, d) -> None:
        self.a, self.b, self.c, self.d = a, b, c, d
        if type(a) == int: self.a, self.b, self.c, self.d = BaseFraction(a, 1), BaseFraction(b, 1), BaseFraction(c, 1), BaseFraction(d, 1)
    def __add__(self, other: 'AdvancedFraction') -> 'AdvancedFraction': a,b,c,d,e,f,g,h = self.a,self.b,self.c,self.d,other.a,other.b,other.c,other.d; return AdvancedFraction(a*h+b*g+c*f+d*e, b*h+d*f, c*h+d*g, d*h)
    def __mul__(self, other: 'AdvancedFraction') -> 'AdvancedFraction': a,b,c,d,e,f,g,h = self.a,self.b,self.c,self.d,other.a,other.b,other.c,other.d; return AdvancedFraction(a*f+b*e, b*f, c*h+d*g, d*h)
    def __sub__(self, other: 'AdvancedFraction') -> 'AdvancedFraction': return self + (-other)
    def __neg__(self): return AdvancedFraction(-self.a, -self.b, self.c, self.d)
    def __truediv__(self, other: 'AdvancedFraction') -> 'AdvancedFraction':
        if other.a == BaseFraction(0, 1) and other.b == BaseFraction(0, 1): raise ZeroDivisionError()
        return self * AdvancedFraction(other.c, other.d, other.a, other.b)
    
def calculatePostFix(statement: list, *optional) -> AdvancedFraction:
    stack, x_in = [], [BaseFraction(0, 1), optional[0], BaseFraction(0, 1), BaseFraction(1, 1)] if optional else [1, 0, 0, 1]
    for e in statement:
        if e in '+-*/':
            right = stack.pop(); left = stack.pop()
            if e == '+': stack.append(left + right)
            elif e == '-': stack.append(left - right)
            elif e == '*': stack.append(left * right)
            elif e == '/': stack.append(left / right)
        elif e == 'X': stack.append(AdvancedFraction(*x_in))
        else: stack.append(AdvancedFraction(0, int(e), 0, 1))
    return stack.pop()

def computeLinearEquation(s: list):
    result = calculatePostFix(s)
    if result.a != BaseFraction(0, 1):
        x = -result.b / result.a
        try: calculatePostFix(s, x); print("X =", str(x))
        except: print("NONE")
    elif result.c != BaseFraction(0, 1): print("MULTIPLE" if result.b == BaseFraction(0, 1) else "NONE")
    elif result.d != BaseFraction(0, 1) and result.b == BaseFraction(0, 1): print("MULTIPLE")
    else: print("NONE")

computeLinearEquation(input().split())