from collections import OrderedDict
class Cache:
    def __init__(self, max_size): self.memory = OrderedDict(); self.max_size = max_size
    def __str__(self): return '\n'.join(map(str, reversed(self.memory)))
    def LRU(self, key, value = None):
        self.memory[key] = value; self.memory.move_to_end(key)
        if len(self.memory) > self.max_size:self.memory.popitem(last=False)

n, m = map(int, input().split())
cache = Cache(m)
for _ in range(n): cache.LRU(int(input()))
print(cache)