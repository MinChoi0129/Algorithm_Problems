import sys
n = int(sys.stdin.readline().rstrip())
crains = map(int, sys.stdin.readline().rstrip().split())
m = int(sys.stdin.readline().rstrip())
boxes = map(int, sys.stdin.readline().rstrip().split())

crains = sorted(crains, reverse=True)
boxes = sorted(boxes, reverse=True)

if max(boxes) > max(crains):
    print(-1)

else: 
    move = 0
    while boxes:
        for crain in crains:
            for box_idx in range(len(boxes)):
                if crain >= boxes[box_idx]:
                    del boxes[box_idx]
                    break
        move += 1

    print(move)