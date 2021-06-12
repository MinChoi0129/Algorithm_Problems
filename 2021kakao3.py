def solution(all_infos, all_queries):

    class Developer:
        def __init__(self, infos):
            splitted_infos = list(infos.split())
            self.lang, self.part, self.level, self.soulfood, self.score = \
                splitted_infos[0], splitted_infos[1], splitted_infos[2], splitted_infos[3], splitted_infos[4] 

    def NumberOfFitCandidates(queries):
        count = 0
        for candidate in candidates:
            if queries[0] != candidate.lang:
                if queries[0] != '-':
                    continue
            if queries[1] != candidate.part:
                if queries[1] != '-':
                    continue
            if queries[2] != candidate.level:
                if queries[2] != '-':
                    continue
            if queries[3] != candidate.soulfood:
                if queries[3] != '-':
                    continue
            if int(queries[4]) <= int(candidate.score):
                count += 1
        return count

    candidates, answer = [], []
    
    for infos in all_infos: # 모든 지원자
        candidates.append(Developer(infos))
        
    for queries in all_queries:
        tmp = queries.split(" and ")
        answer.append(NumberOfFitCandidates([tmp[0], tmp[1], tmp[2], tmp[3].split()[0], tmp[3].split()[1]]))
    
    return answer