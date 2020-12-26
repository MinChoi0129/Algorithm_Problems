import sys

def words_appending(puzzle):
    global words

    for data in puzzle:
        if "#" not in data:
            text = ""
            for i in data:
                text += i
            words.append(text)
        else:
            text = ""
            for char in data:
                if char != "#":
                    text += char
                else:
                    if len(text) >= 2:
                        words.append(text)
                    text = ""
            if len(text) >= 2: # 길이가 2 이상인데, for문이 끝나버려 #을 만나지 못한 경우 append
                words.append(text)

words = []
puzzle_horizon = []
puzzle_vertical = []

r, c = map(int, sys.stdin.readline().rstrip().split())

for _ in range(r): # 단어를 가로로 볼 때
    puzzle_horizon.append(list(sys.stdin.readline().rstrip()))
    
for y in range(c): # 단어를 세로로 볼 때
    tmp = []
    for x in range(r):
        tmp.append(puzzle_horizon[x][y])
    puzzle_vertical.append(tmp)


words_appending(puzzle_horizon)
words_appending(puzzle_vertical)

words.sort()
print(words[0])