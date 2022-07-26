def cubing(face, direction):
    global u, d, l, r, f, b
    if direction == '+':
        if face == 'U':
            u = [[u[2-y][x] for y in range(3)] for x in range(3)]
            tmp_line = [f[0][i] for i in range(3)]
            for i in range(3):
                f[0][i] = r[0][i]
                r[0][i] = b[0][i]
                b[0][i] = l[0][i]
                l[0][i] = tmp_line[i]
        elif face == 'D':
            d = [[d[2-y][x] for y in range(3)] for x in range(3)]
            tmp_line = [b[2][i] for i in range(3)]
            for i in range(3):
                b[2][i] = r[2][i]
                r[2][i] = f[2][i]
                f[2][i] = l[2][i]
                l[2][i] = tmp_line[i]
        elif face == 'L':
            l = [[l[2-y][x] for y in range(3)] for x in range(3)]
            tmp_line = [b[2-i][2] for i in range(3)]
            for i in range(3):
                b[2-i][2] = d[i][0]
                d[i][0] = f[i][0]
                f[i][0] = u[i][0]
                u[i][0] = tmp_line[i]
        elif face == 'R':
            r = [[r[2-y][x] for y in range(3)] for x in range(3)]
            tmp_line = [f[2-i][2] for i in range(3)]
            for i in range(3):
                f[2-i][2] = d[2-i][2]
                d[2-i][2] = b[i][0]
                b[i][0] = u[2-i][2]
                u[2-i][2] = tmp_line[i]
        elif face == 'F':
            f = [[f[2-y][x] for y in range(3)] for x in range(3)]
            tmp_line = [d[0][2-i] for i in range(3)]
            for i in range(3):
                d[0][2-i] = r[i][0]
                r[i][0] = u[2][i]
                u[2][i] = l[2-i][2]
                l[2-i][2] = tmp_line[i]
        elif face == 'B':
            b = [[b[2-y][x] for y in range(3)] for x in range(3)]
            tmp_line = [u[0][2-i] for i in range(3)]
            for i in range(3):
                u[0][2-i] = r[2-i][2]
                r[2-i][2] = d[2][i]
                d[2][i] = l[i][0]
                l[i][0] = tmp_line[i]
    else: # direction == '-
        for _ in range(3):
            cubing(face, '+')

for _ in range(int(input())):
    u, d, l, r, f, b = \
    [['w'] * 3 for _ in range(3)],\
    [['y'] * 3 for _ in range(3)],\
    [['g'] * 3 for _ in range(3)],\
    [['b'] * 3 for _ in range(3)],\
    [['r'] * 3 for _ in range(3)],\
    [['o'] * 3 for _ in range(3)]
    int(input())
    for command in input().split(): cubing(command[0], command[1])
    for line in u:
        for element in line:
            print(element, end = "")
        print()