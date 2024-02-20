def solution(strings, n):
    # key= 파라미터를 이용하여 원하는 키로 정렬 가능
    return sorted(strings, key=lambda x: (x[n], x))
