import heapq


def find(computer):
    if computer == root[computer]:
        return computer
    else:
        root[computer] = find(root[computer])
        return root[computer]


n, m = int(input()), int(input())
root = {computer: computer for computer in range(1, n + 1)}
edges = []

for _ in range(m):
    computer_a, computer_b, distance = map(int, input().split())
    heapq.heappush(edges, (distance, computer_a, computer_b))

minimum_distance = 0
while edges:
    distance, computer_a, computer_b = heapq.heappop(edges)
    root_of_a, root_of_b = find(computer_a), find(computer_b)
    if root_of_a == root_of_b:  # 사이클
        continue
    else:
        minimum_distance += distance
        if root_of_a < root_of_b:
            root[root_of_b] = root_of_a
        elif root_of_a > root_of_b:
            root[root_of_a] = root_of_b

print(minimum_distance)
