import sys, heapq

INF = int(1e9)
input = lambda : sys.stdin.readline().rstrip()

def extractHackingResults(results):
    hacked_computer, max_hacking_time = 0, 0
    for hacking_time in results:
        if hacking_time not in [None, INF]:
            hacked_computer += 1
            max_hacking_time = max(max_hacking_time, hacking_time)
    
    return hacked_computer, max_hacking_time

def getDijkstraHackingTime(number_of_computers, connections, first_hacked_computer):
    hacking_times = [None] + [INF] * number_of_computers
    hacking_times[first_hacked_computer] = 0

    Q = [(0, first_hacked_computer)]
    while Q:
        _, present_computer = heapq.heappop(Q)
        for adj_computer, adj_hacking_time in connections[present_computer]:
            if hacking_times[adj_computer] > hacking_times[present_computer] + adj_hacking_time:
                hacking_times[adj_computer] = hacking_times[present_computer] + adj_hacking_time
                heapq.heappush(Q, (hacking_times[adj_computer], adj_computer))
    
    return hacking_times

for _ in range(int(input())):
    number_of_computers, dependencies, first_hacked_computer = map(int, input().split())

    connections = {computer: [] for computer in range(1, number_of_computers + 1)}
    for _ in range(dependencies):
        to_computer, from_computer, hacking_time = map(int, input().split())
        connections[from_computer].append((to_computer, hacking_time))
    
    results = getDijkstraHackingTime(number_of_computers, connections, first_hacked_computer)
    print(*extractHackingResults(results))