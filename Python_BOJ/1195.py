from collections import deque

def isKickDown(up_line, down_line, total_size):
    for i in range(total_size):
        if int(up_line[i]) + int(down_line[i]) == 4: return False
    return True
    
def getKickDownSize(up_line, down_line, total_size):
    for i in range(total_size):
        if up_line[i] == '0' and down_line[i] == '0': total_size -= 1
    return total_size

def main():
    line_a, line_b = list(input()), list(input())
    up_line, down_line = (line_a, line_b) if len(line_a) <= len(line_b) else (line_b, line_a)
    l1, l2 = len(up_line), len(down_line) # 항상 l1 이 짧거나 같도록.
    up_line, down_line = deque(up_line + ['0'] * (l2 - 1) + ['0'] * (l1 - 1)), deque(['0'] * (l1 - 1) + down_line + ['0'] * (l1 - 1))
    min_size = default_size = 2 * l1 + l2 - 2

    if l1 == 1:
        if up_line[0] == '1': return l2
        else: return l2 + 1 if down_line.count('1') == 0 else l2

    for i in range(default_size):
        if isKickDown(up_line, down_line, default_size):
            min_size = min(min_size, getKickDownSize(up_line, down_line, default_size))
        up_line.appendleft(up_line.pop())

    return min_size if min_size != default_size else (min_size + 1)

print(main())