def solution(record):
    logs, id_nickname_update = [], dict()
    for i in range(len(record)):
        try:
            status, raw_id, nickname = record[i].split()
        except:
            status, raw_id = record[i].split()
        if status == "Change" or status == "Enter":
            id_nickname_update[raw_id] = nickname
        logs.append((status, raw_id)) # 순서, 상태, 고유번호
        
    answer = []
    for log in logs:
        if log[0] == "Enter":
            answer.append(id_nickname_update[log[1]] + "님이 들어왔습니다.")
        elif log[0] == "Leave":
            answer.append(id_nickname_update[log[1]] + "님이 나갔습니다.")
    
    return answer