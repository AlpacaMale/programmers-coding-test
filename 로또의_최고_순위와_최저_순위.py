def solution(lottos, win_nums):
    overlap_count = len(set(lottos) & set(win_nums))
    zero_count = lottos.count(0)
    return [min(7 - overlap_count - zero_count, 6), min(7 - overlap_count, 6)]