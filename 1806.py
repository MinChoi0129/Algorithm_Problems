# n, s = map(int, input().split())
# arr = [*map(int, input().split())]

# gap = 1
# p1 = 0
# p2 = p1 + gap

# while True:
#     if sum(arr[p1 : p2 + 1]) >= s:
#         print(gap + 1)
#         break
        
#     if gap == n - 1:
#         break
        
#     if p2 == n - 1:
#         p1 = 0
#         gap += 1
#         p2 = p1 + gap

#     else:
#         p1 += 1; p2 = p1 + gap