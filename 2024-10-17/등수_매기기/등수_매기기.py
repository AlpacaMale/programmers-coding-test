from collections import Counter


def solution(score):
    total_scores = [eng + math for eng, math in score]
    total_freq = Counter(total_scores)
    sorted_total_list = sorted(total_freq, key=lambda x: -x)
    ranks = {}
    rank = 1
    for total in sorted_total_list:
        ranks[total] = rank
        rank += total_freq[total]

    return [ranks[total] for total in total_scores]
