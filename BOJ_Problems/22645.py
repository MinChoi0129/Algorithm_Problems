from collections import OrderedDict
class Cache:
    def __init__(self, max_size):
        self.memory = OrderedDict()
        self.max_size = max_size
    def __str__(self):
        return '\n'.join(map(str, reversed(self.memory)))
    def LRU(self, key, value = None):
        self.memory[key] = value
        self.memory.move_to_end(key)
        if len(self.memory) > self.max_size:
            self.memory.popitem(last=False)

n, m = map(int, input().split())
cache = Cache(m)
for _ in range(n): cache.LRU(int(input()))
print(cache)

class Cache:
    def __init__(self, max_size):
        self.memory = []
        self.current_size = 0
        self.max_size = max_size
    def __str__(self):
        return '\n'.join(map(str, reversed(self.memory)))
    def LRU(self, value):
        for i in range(self.current_size):
            if self.memory[i] == value:
                self.memory.pop(i)
                self.current_size -= 1
                break
        
        if self.current_size < self.max_size: self.current_size += 1
        else: self.memory.pop(0)

        self.memory.append(value)

n, m = map(int, input().split())
cache = Cache(m)
for _ in range(n):
    cache.LRU(int(input()))
print(cache)