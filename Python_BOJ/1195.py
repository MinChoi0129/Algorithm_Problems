from collections import deque

def isKickDown(up_line, down_line, total_size):
    for i in range(total_size):
        if int(up_line[i]) + int(down_line[i]) == 4: return False
    return True
    
def getKickDownSize(up_line, down_line, total_size):
    for i in range(total_size):
        if up_line[i] == '0' and down_line[i] == '0': total_size -= 1
    return total_size

def main(lines, given_answer):
# def main():
    
    # line_a, line_b = list(input()), list(input())
    
    # @@@TEST@@@ 
    line_a, line_b = lines
    
    up_line, down_line = (line_a, line_b) if len(line_a) <= len(line_b) else (line_b, line_a)
    l1, l2 = len(up_line), len(down_line) # 항상 l1 이 짧거나 같은 것
    up_line, down_line = deque(up_line + ['0'] * (l2 - 1) + ['0'] * (l1 - 1)), deque(['0'] * (l1 - 1) + down_line + ['0'] * (l1 - 1))
    min_size = default_size = 2*l1 + l2 - 2
    
    if l1 == 1: min_size = default_size = l2

    for i in range(default_size):
        if isKickDown(up_line, down_line, default_size):
            min_size = min(min_size, getKickDownSize(up_line, down_line, default_size))
        up_line.appendleft(up_line.pop())
    
    answer = min_size if min_size != default_size else (min_size + 1)
    if answer != int(given_answer): print(answer, given_answer)
    
    # @@@TEST@@@ 
    # print(min_size if min_size != default_size else (min_size + 1))
    
# main()