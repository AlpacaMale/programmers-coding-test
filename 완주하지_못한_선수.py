#카운터 없이 해보기

def solution(participant, completion):
    participant_count = Counter(participant)
    for completion_name in completion:
        participant_count[completion_name] -= 1
    return [key for key, value in participant_count.items() if value == 1][0]


def Counter(list_):
    list_count = {}
    for element in list_:
        if element not in list_count:
            list_count[element] = 1
        else:
            list_count[element] += 1
    return list_count


from collections import Counter


def solution(participant, completion):
    participant_count = Counter(participant)
    completion_count = Counter(completion)
    return list((participant_count - completion_count).keys())[0]
