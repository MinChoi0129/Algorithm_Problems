from collections import deque

class Browser:
    def __init__(self):
        self.back, self.current, self.front = deque(), None, deque()
    def go_back(self):
        if self.back:
            self.front.appendleft(self.current)
            self.current = self.back.pop()
    def go_front(self):
        if self.front:
            self.back.append(self.current)
            self.current = self.front.popleft()
    def enter(self, page):
        self.front.clear()
        if self.current != None:
            self.back.append(self.current)
        self.current = page
    def compress(self):
        for i in range(len(self.back) - 1):
            if self.back[i] == self.back[i+1]:
                self.back[i] = None
        self.back = deque([e for e in self.back if e != None])

n, q = map(int, input().split())
browser = Browser()
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