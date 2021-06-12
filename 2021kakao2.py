def solution(orders, course):
    from itertools import combinations
    answers, real_answers = [], []
    menus, combis = set(), []

    for order in orders:
        for letter in order:
            menus.add(letter)

    for num in course:
        combis.append([*combinations(menus, num)])
    combis = sum(combis, [])
    
    for combi in combis:
        subsetCount = 0
        for order in orders:
            t1, t2 = set(combi), set(order)
            if t1.issubset(t2):
                subsetCount += 1
        if subsetCount >= 2:
            t3 = "".join(sorted(list(combi)))
            answers.append((t3, len(t3), subsetCount))

    answers.sort(key = lambda x : (x[1], -x[2]))
    last_length, max_times = answers[0][1], answers[0][2]
    for i in range(len(answers)):
        if answers[i][1] > last_length:
            last_length = answers[i][1]
            max_times = answers[i][2]
        if answers[i][1] == last_length:
            if answers[i][2] < max_times:
                answers[i] = ()

    for answer in answers:
        if answer:
            real_answers.append(answer[0])

    return sorted(real_answers)