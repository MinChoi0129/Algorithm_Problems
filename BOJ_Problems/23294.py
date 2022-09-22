from collections import deque

class Browser:
    def __init__(self, max_cache_size):
        self.back = deque()
        self.current = None
        self.front = deque()
        self.current_cache_size = 0
        self.MAX_CACHE_SIZE = max_cache_size
    def go_back(self):
        if self.back:
            self.front.appendleft(self.current)
            self.current = self.back.pop()
        self.calculateCurrentCacheSize()
    def go_front(self):
        if self.front:
            self.back.append(self.current)
            self.current = self.front.popleft()
        self.calculateCurrentCacheSize()
    def enter(self, page):
        self.front.clear()

        if self.current != None:
            self.back.append(self.current)
        self.current = page
        
        while self.calculateCurrentCacheSize() > self.MAX_CACHE_SIZE:
            self.back.popleft()
        self.calculateCurrentCacheSize()
    def compress(self):
        for i in range(len(self.back) - 1):
            if self.back[i] == self.back[i+1]:
                self.back[i] = None
        self.back = deque([e for e in self.back if e != None])
        self.calculateCurrentCacheSize()
    def calculateCurrentCacheSize(self):
        total_cache_size = cache_size_by_sites[int(self.current if self.current != None else 0)]
        for d in [self.back, self.front]:
            for site in d:
                total_cache_size += cache_size_by_sites[int(site)]
        self.current_cache_size = total_cache_size
        return total_cache_size

n, q, c = map(int, input().split())
cache_size_by_sites = [None] + [*map(int, input().split())]
browser = Browser(c)
for _ in range(q):
    command = input().split()
    if command[0] == 'B': browser.go_back()
    elif command[0] == 'F': browser.go_front()
    elif command[0] == 'C': browser.compress()
    else: browser.enter(command[1])

print(browser.current)
if browser.back: print(*reversed([e for e in browser.back]))
else: print(-1)
if browser.front: print(*[e for e in browser.front])
else: print(-1)