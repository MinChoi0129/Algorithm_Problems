def PI_s_square(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    try:
        m = (y2-y1) / (x2-x1)
        n = y1 - m*x1
        integral = m*m*((x2)**3 - (x1)**3)/3 + m*n*((x2)**2 - (x1)**2) + n*n*(x2-x1)
        return PI * integral
    except: return 0

def getVolume(points):
    points.sort()
    volume = PI_s_square(points[0], points[2])
    volume -= PI_s_square(points[0], points[1])
    volume -= PI_s_square(points[1], points[2])
    return abs(volume)

PI = 3.14159265358979
x1, y1, x2, y2, x3, y3 = map(int, input().split())
a = getVolume([[x1, y1], [x2, y2], [x3, y3]])
b = getVolume([[y1, x1], [y2, x2], [y3, x3]])
print(a, b)