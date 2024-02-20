def solution(arr, n):
    result = []
    is_odd = len(arr) % 2
    for index, number in enumerate(arr):
        # arr의 길이가 홀수(is_odd)면서 짝수번째 인덱스(not index%2)거나
        # arr의 길이가 짝수(not is_odd)면서 홀수번째 인덱스일때, n을 더해서 새로운 배열을 만들어줌
        if (is_odd and not index % 2) or (not is_odd and index % 2):
            result.append(number + n)
        else:
            result.append(number)
    return result
