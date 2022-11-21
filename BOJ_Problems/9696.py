# for i in range(int(input())):
#     print("Case #%d:" % (i+1), end = " ")

#     statement = input()
#     answer = eval(statement)
    
#     statement = [e for e in statement.split() if e in "+-*/"]
#     stack = []
#     for e in statement:
#         if e in "+-":
#             stack.append(e)
#         else:
#             while stack and stack[-1] in "*/":
#                 print(stack.pop(), end = " ")
#             stack.append(e)
#     while stack:
#         print(stack.pop(), end = " ")
#     print()