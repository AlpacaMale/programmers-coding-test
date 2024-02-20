def solution(n):
    n_3 = ""
    # n진법 구하는 공식은 이 코드에서 최종적으로 reverse해줘야하지만 그러지 않았다
    while n != 0:
        x = str(n % 3)
        n //= 3
        n_3 += x
        # int의 두번째 인자에 숫자n을 넘기면 n진법에서 10진법으로 변환이 가능하다
    return int(n_3, 3)
