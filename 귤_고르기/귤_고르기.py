from collections import Counter


def solution(k, tangerine):
    # Conter는 리스트에 중복된 값이 몇번 나왔는지 세주는 함수
    counts = Counter(tangerine)
    counts_list = list(sorted(counts.values(), reverse=True))
    length = len(counts_list)
    size = 0
    sum_tangerine = 0
    # 언제 끝이 나는지 모르는 반복은 while문을 통해 조건을 걸어준다
    while size < length and sum_tangerine < k:
        sum_tangerine += counts_list[size]
        size += 1
    return size
