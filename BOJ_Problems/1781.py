import heapq

# 당연한 사실 : 숙제 많이 할 수록 컵라면도 더 받을 수 있다.


# 컵라면 개수에 눈 돌아가지 말고 양치기를 하자.
#   -> 데드라인 짧은것부터 많이 풀기(정렬)


# 근데 마감기한 때문에 숙제를 못하는 상황이 생긴다면
# 숙제를 버려야 하는데 이왕 버리는거 컵라면 많이 안주는걸 버리자.
#   -> 컵라면 적게주는것부터 풀기(정렬)


# 먼저 버리려면 당연한 얘기겠지만 먼저 담겨있어야 하겠지?
#   -> sorting(정렬) 관련...


# 컵라면 적게주는것부터 숙제를 도전하다가 시간때문에 안되면
# 컵라면 제일 적게주는걸(min...??) 버리자.
#   -> pop 관련...,

n = int(input())
homeworks = sorted([[*map(int, input().split())] for _ in range(n)])

task = []  # 풀 숙제들의 컵라면 개수를 담을 힙 공간
for deadline, number_of_cup_ramen in homeworks:
    # 무지성으로 일단 한개 담기 / heap이니까 버려도 제일 가치없는거(컵라면 개수 적은거) 버리게될거임
    heapq.heappush(task, number_of_cup_ramen)

    number_of_task = len(task)
    if deadline < number_of_task:  # 시간 내에 못푸는 숙제가 생긴다면
        heapq.heappop(task)  # 과감히 가치 없는 문제 버리기

print(sum(task))  # 컵라면 개수 총합 출력
