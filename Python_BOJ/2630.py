import sys
input = lambda : sys.stdin.readline().rstrip()

def is_perfect(paper):
    zero_zero = paper[0][0]
    for line in paper:
        for element in line:
            if element != zero_zero:
                return False
    return True
        
def cut(paper):
    papers = []
    length = len(paper)
    for i in range(length):
        
paper = []

N = int(input())
for _ in range(N):
    paper.append(input().split())
    
if is_perfect(paper):
    