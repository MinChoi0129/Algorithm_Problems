def solution(genres, plays):
    genres_chart = dict()

    for i in range(len(genres)):
        if genres[i] not in genres_chart: genres_chart[genres[i]] = [(plays[i], i)]
        else: genres_chart[genres[i]].append((plays[i], i))

    for value in genres_chart.values(): value.sort(key = lambda x : (-x[0], x[1]))

    for value in genres_chart.values():
        popularity = 0
        for song in value: popularity += song[0]
        value.append(popularity)

    answer = []
    for result in sorted(genres_chart.items(), key = lambda x : x[1][-1], reverse=True):
        tmp = []
        for song in result[1]:
            try: 
                tmp.append(song[1])
                if len(tmp) == 2: break
            except: break
        answer += tmp
    
    return answer