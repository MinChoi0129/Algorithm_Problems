def solution(new_id):
    rule_chr = "abcdefghijklmnopqrstuvwxyz0123456789-_."
    answer = "".join(new_id)

    def isConditional():
        if answer.startswith(".") or answer.endswith("."):
            return False
        if not (3 <= len(answer) <= 15):
            return False
        if ".." in answer:
            return False
        for i in answer:
            if i not in rule_chr:
                return False
        return True

    while not isConditional():
        # STEP 1
        answer = list(answer.lower())

        # STEP 2
        for idx in range(len(answer)):
            if answer[idx] not in rule_chr:
                answer[idx] = '""'
        while '""' in answer:
            answer.remove('""')

        # STEP 3
        answer = "".join(answer)
        while ".." in answer:
            answer = answer.replace("..", '.')

        # STEP 4
        answer = list(answer)
        if len(answer) >= 1 and answer[0] == '.':
            answer.pop(0)
        if len(answer) >= 1 and answer[-1] == '.':
            answer.pop(-1)

        # STEP 5
        if len(answer) == 0:
            answer = 'a'

        # STEP 6
        if len(answer) >= 16:
            answer = answer[:15]

        # STEP 7
        answer = list(answer)
        while len(answer) <= 2:
            answer.append(answer[-1])
        answer = "".join(answer)

    return answer