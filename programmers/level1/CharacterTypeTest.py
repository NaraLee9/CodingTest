from collections import Counter

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

def solution(survey, choices):
    types  = Counter({c:0 for c in "RTCFJMAN"}) # 생성되지 않은 key로 인하여 pair 순회 중 키가 없으면 오류 발생
    answer =  ''
    for i in range(len(choices)):
        score = choices[i] - 4 # 0, 3 - -3
        if score == 0:
            continue
        target = survey[i][0] if score < 0 else survey[i][1]
        types[target] += abs(score)

    pairs = [('R','T'),('C','F'),('J','M'),('A','N')]

    for a,b in pairs:
        if types[a] >= types[b]:
            answer += a
        else:
            answer += b

    return answer

solution(survey, choices)


survey = ["TR", "RT", "TR"]
choices = [7, 1, 3]

def solution_2(survey, choices):
    types = {c: 0 for c in "RTCFJMAN"}
    answer = ''

    for i in range(len(choices)):
        score = choices[i] - 4
        if score == 0:
            continue
        target = survey[i][0] if score < 0 else survey[i][1]
        types[target] += abs(score)

    pairs = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]

    for a, b in pairs:
        if types[a] >= types[b]:
            answer += a
        else:
            answer += b

    return answer




solution_2(survey, choices)