R, C = map(int, input().split())

def ReadWordHorizontal(data):
    for line in data:
        tmp = ""
        for char in line:
            if char != "#":
                tmp += char
            else:
                if len(tmp) >= 2:
                    words.append(tmp)
                tmp = ""
        if len(tmp) >= 2: # 길이가 2 이상인데, for문이 끝나버려 #을 만나지 못한 경우 append
                words.append(tmp)

def ReadWordVertical(data):
    h = len(data)
    w = len(data[0])
    for y in range(w):
        tmp = ""
        for x in range(h):
            if data[x][y] != "#":
                tmp += data[x][y]
            else:
                if len(tmp) >= 2:
                    words.append(tmp)
                tmp = ""
        if len(tmp) >= 2: # 길이가 2 이상인데, for문이 끝나버려 #을 만나지 못한 경우 append
                words.append(tmp)

puzzle = []
words = []

for _ in range(R):
    puzzle.append(list(input()))

ReadWordHorizontal(puzzle)
ReadWordVertical(puzzle)

words.sort()
print(words[0])