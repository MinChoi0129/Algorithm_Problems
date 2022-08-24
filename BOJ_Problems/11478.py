s = input()
words = set(i for i in s)
for i in range(len(s)-1):
    for j in range(i+2, len(s)+1):
        words.add(s[i:j])
print(len(words))