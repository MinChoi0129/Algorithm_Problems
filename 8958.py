n = int(input())

def score(answer):
    O_score = 1  # O 점수
    my_score = 0  # 내 점수

    for i in range(len(answer)):
        if answer[i] == 'O':
            my_score += O_score
            O_score += 1
        else:
            O_score = 1

    return my_score


for _ in range(n):
    print(score(input()))