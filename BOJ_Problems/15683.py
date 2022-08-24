import itertools, copy

def getSurveillanceRange(office, case, cctvs):
    for i in range(len(cctvs)):
        for direction in case[i]:
            cctv_x, cctv_y = cctvs[i]
            if direction in 'ud':
                dx, limit = [-1, -1] if direction == 'u' else [1, len(office)]
                for x in range(cctv_x + dx, limit, dx):
                    if office[x][cctv_y] == '6': break
                    else: office[x][cctv_y] = '#'       
            else:
                dy, limit = [-1, -1] if direction == 'l' else [1, len(office[0])]
                for y in range(cctv_y + dy, limit, dy):
                    if office[cctv_x][y] == '6': break
                    else: office[cctv_x][y] = '#'           
    return sum([line.count('0') for line in office])

n, m = map(int, input().split())
office, cctvs, directions = [list(input().split()) for _ in range(n)], [], []

for x in range(n):
    for y in range(m):
        element = office[x][y]
        if element == '1': directions.append(['u', 'r', 'd', 'l'])
        elif element == '2': directions.append(['ud', 'lr'])
        elif element == '3': directions.append(['ur', 'rd', 'dl', 'lu'])
        elif element == '4': directions.append(['lur', 'urd', 'rdl', 'dlu'])
        elif element == '5': directions.append(['urdl'])
        if element in "12345": cctvs.append([x, y])

answer = n*m
for case in itertools.product(*directions):
    answer = min(answer, getSurveillanceRange(copy.deepcopy(office), case, cctvs))
print(answer)