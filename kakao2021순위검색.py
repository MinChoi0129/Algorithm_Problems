from typing import NewType


def solution(all_infos, all_queries):
    languages = {'cpp':set(), 'java':set(), 'python':set(), '-':set(range(len(all_infos)))}
    side = {'backend':set(), 'frontend':set(), '-':set(range(len(all_infos)))}
    level = {'junior':set(), 'senior':set(), '-':set(range(len(all_infos)))}
    food = {'chicken':set(), 'pizza':set(), '-':set(range(len(all_infos)))}
    scores = [0] * len(all_infos)
    for i in range(len(all_infos)):
        for j in all_infos[i].split():
            if j in languages: languages[j].add(i)
            elif j in side: side[j].add(i)
            elif j in level: level[j].add(i)
            elif j in food: food[j].add(i)

            try: scores[i] = int(j)
            except: continue
    
    answer = []
    for human in all_queries:
        human = human.replace("and", "").split()
        tmpLang, tmpSide, tmpLv, tmpFood = human[0], human[1], human[2], human[3]
        
        count = 0
        for i in languages[tmpLang] & side[tmpSide] & level[tmpLv] & food[tmpFood]:
            if scores[i] >= int(human[4]): count += 1
        answer.append(count)          
    return answer
                    
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))