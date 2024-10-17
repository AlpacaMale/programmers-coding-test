def solution(numbers, k):
    index = (k - 1) * 2 % len(numbers)
    return numbers[index]
