participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

from collections import Counter

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(participant)-1):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[- 1]

solution(participant, completion)

cnt = Counter()

def solution_2(participant, completion):

    for p in participant:
        cnt[p] += 1
    for c in completion:
        cnt[c] -= 1

    for k,v in cnt.items():
        if v > 0:
            return k

solution_2(participant,completion)

def solution_3(participant, completion):

    answer = Counter(participant) - Counter(completion)

    return list(answer.keys())[0]

solution_3(participant,completion)