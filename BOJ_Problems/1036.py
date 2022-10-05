digits_36 = {str(i):0 for i in range(10)}
for i in range(65, 91): digits_36[chr(i)] = 0

words = []
for _ in range(int(input())):
    word = list(input())
    for char in word:
        digits_36[char] += 1
    words.append(word)
k = int(input())