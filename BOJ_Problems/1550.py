hex = {str(i):i for i in range(10)}
hex.update({'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15})

result = 0
for idx, char in enumerate(reversed(input())):
    result += (16 ** idx) * hex[char]
print(result)