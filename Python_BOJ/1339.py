# 초기화
words, alphabets = [], dict()
for i in range(65, 91):
    alphabets[chr(i)] = 0

# 입력
for _ in range(int(input())):
    words.append(input())

# 알파벳마다 갖고 있는 자리수를 value化 한 것
for word in words:
    length = len(word)
    for i in range(len(word)):
        alphabets[word[i]] += 10 ** (length - (i+1))

# value가 존재(>0) 하는 것만 추출 후 내림차순 정렬
usingAlphabets = []
for val in alphabets.values():
    if val > 0:
        usingAlphabets.append(val)

usingAlphabets.sort(reverse=True)

# 큰 수(9) 부터 하나씩 곱해줌
total = 0
for i in range(len(usingAlphabets)):
    total += usingAlphabets[i] * (9 - i)
    
# 결과
print(total)