# import heapq

# for _ in range(int(input())): # test case
#     parts = dict()
#     nop, budget = map(int, input().split())
#     for _ in range(nop): # number of parts
#         tmp = input().split()
#         if tmp[0] not in parts:
#             parts[tmp[0]] = [[int(tmp[3]), int(tmp[2])]]
#         else:
#             heapq.heappush(parts[tmp[0]], [int(tmp[3]), int(tmp[2])])
    
#     selected_parts = dict()
#     total_price = 0
#     total_quality = 0
#     for part in parts.keys():
#         quality, price = heapq.heappop(parts[part])
#         if part not in selected_parts:
#             selected_parts[part] = quality
#             total_price += price
#             total_quality += quality
#         else:
#             if total_price + price <= budget:
#                 sele
                

        