import heapq

a = [1,5,2,10,-99,7,5]
b = [-i for i in a]
heapq.heapify(a)
heapq.heapify(b)
print(a)
print("[", end = "")
for i in b:
    print(-i, end = ", ")
print("]")