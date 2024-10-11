def solution(a, b):
    #max함수는 두 수를 비교해서 큰 값을 리턴하는 함수
    return max(int(str(a) + str(b)), 2 * a * b)
