def solution(ranks, attendance):
    preference = {}
    for index, rank in enumerate(ranks):
        if attendance[index]:
            preference[rank] = index
    ranker = sorted(preference.keys())[:3]
    return (
        preference[ranker[0]] * 10000
        + preference[ranker[1]] * 100
        + preference[ranker[2]]
    )
