for _ in range(int(input())):
    n, m = map(int, input().split())
    book = {i + 1 : 1 for i in range(n)}
    stu_cnt = 0
    for stu in sorted([[*map(int, input().split())] for _ in range(m)], key = lambda x : x[1]):
        for idx in range(stu[0], stu[1] + 1):
            if book[idx]:
                book[idx] = 0
                stu_cnt += 1
                break    
    print(stu_cnt)