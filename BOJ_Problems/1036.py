# from collections import deque

# digits_36 = {str(i): i for i in range(10)}
# for num in range(65, 91):
#     digits_36[chr(num)] = num - 55


# n, words_in_decimal, max_length = int(input()), [], 0
# for _ in range(n):
#     word = list(input())
#     word_in_decimal = deque()
#     max_length = max(max_length, len(word))
#     for letter in word:
#         word_in_decimal.append(digits_36[letter])
#     words_in_decimal.append(word_in_decimal)

# for word_in_decimal in words_in_decimal:
#     for _ in range(max_length - len(word_in_decimal)):
#         word_in_decimal.appendleft(0)

# k = int(input())

# while k:
#     for y in range(max_length):
#         for x in range(n):


#     k -= 1