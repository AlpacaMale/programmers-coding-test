def solution(arr, divisor):
    # 빈 배열이면 false이므로 or를 사용가능
    return sorted(number for number in arr if not number % divisor) or [-1]
