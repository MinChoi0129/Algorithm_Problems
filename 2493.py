n = int(input())
towers = [*map(int, input().split())]
stack = []

for i in range(len(towers)):
    height, number = towers[i], i + 1
    if not stack:
        print(0, end = " ")
        stack.append({'height' : height, 'number' : number})
    else:
        while stack:
            recentTower = stack[-1]
            if recentTower['height'] <= height:
                stack.pop()
                if not stack:
                    print(0, end = " ")
            elif recentTower['height'] > height:
                print(recentTower['number'], end = " ")
                break
        stack.append({'height' : height, 'number' : number})