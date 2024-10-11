def solution(s):
    buffer = []
    for char in s:
        if buffer and buffer[-1] == char:
            buffer.pop()
        else:
            buffer.append(char)
    return (not buffer) / 1


# 위의 코드는 리스트로 구현한것이고 아래의 코드는
# 같은 문제를 문자열로 구현한것이다.
# 문자열은 수정할 수 없는(immutable) 자료형이기 때문에
# buffer[:-1]의 연산을 사용하면 O[n]의 시간복잡도가 걸리지만
# buffer.pop()함수는 o[1]의 시간복잡도를 가져 처리할것이
# 많을수록 성능차이는 현격히 나게된다.


def solution(s):
    buffer = ""
    for char in s:
        if buffer and buffer[-1] == char:
            buffer = buffer[:-1]
        else:
            buffer += char
    return (not buffer) / 1
