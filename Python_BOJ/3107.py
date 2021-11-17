# short_ipv6 = list(input().split(':'))
# answer = ["" for _ in range(8)]
# is_0000_used = False

# i = 0
# insert_count = 0
# while i <= 8:
#     try:
#         if len(short_ipv6[i - insert_count]) == 4:
#             answer[i] = short_ipv6[i - insert_count]
#         elif len(short_ipv6[i - insert_count]) > 0:
#             answer[i] = '0' * (4 - len(short_ipv6[i - insert_count])) + short_ipv6[i - insert_count]
#         elif len(short_ipv6[i - insert_count]) == 0: # 빈칸 : ""
#             if is_0000_used:
#                 answer[i] = "0000"
#             else:
#                 count = 0
#                 for string in short_ipv6:
#                     if string != "":
#                         count += 1
#                 answer.pop(i)
#                 for _ in range(8 - count):
#                     answer.insert(i, "0000")
#                     insert_count += 1
#                     i += 1
#                 is_0000_used = True         
#         i += 1
#     except:
#         break
# print(answer)