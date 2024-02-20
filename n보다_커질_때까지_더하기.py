def solution(numbers, n):
    result = 0
    index = 0
    while result <= n:
        result += numbers[index]
        index += 1
    return result
