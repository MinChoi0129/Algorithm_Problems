from collections import deque

def bfs(from_number: str, to_number: str):
    visited = [False] * 10000
    visited[int(from_number)] = True
    Q = deque([[from_number, 0]])

    while Q:
        current_number, count = Q.popleft()
        if current_number == to_number:
            return count
        
        for i in range(4):
            for j in range(10):
                new_number = int(current_number[:i] + str(j) + current_number[i+1:])
                if not visited[new_number] and 9999 >= new_number >= 1000 and is_primes[new_number]:
                    Q.append([str(new_number), count + 1])
                    visited[new_number] = True

    return False

is_primes = [False, False] + [True] * 9998
for i in range(2, 10000):
    if is_primes[i]:
        for j in range(i+i, 10000, i):
            is_primes[j] = False

numbers = [input().split() for _ in range(int(input()))]
for from_number, to_number in numbers:
    if from_number != to_number:
        result = bfs(from_number, to_number)
        print("Impossible" if not result else result)
    else: print(0)