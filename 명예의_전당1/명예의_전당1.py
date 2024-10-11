def solution(k, score):
    # index+1일째의 랭크를 정렬한 후 k명까지 랭크를 표시 후 가장 낮은 랭크의 점수를 차례로 넣은 리스트를 리턴
    return [min(sorted(score[: index + 1])[-k:]) for index, value in enumerate(score)]
