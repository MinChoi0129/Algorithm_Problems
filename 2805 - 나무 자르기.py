n, m = map(int, input().split())
trees = list(map(int, input().split()))

def cut(cut_height):
    stack = 0
    for tree in trees:
        if tree > cut_height:
            stack += (tree - cut_height)
    return stack

def BS(m):
    start = 0
    end = max(trees)
    answer = []
    while start <= end:
        mid = (start + end) // 2
        if cut(mid) >= m:
            start = mid + 1
            answer.append(mid)
        else:
            end = mid - 1
    return max(answer)

print(BS(m))