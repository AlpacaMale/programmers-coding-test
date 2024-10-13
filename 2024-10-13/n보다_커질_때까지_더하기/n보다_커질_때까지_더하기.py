def solution(numbers, n):
    total_sum = 0
    for number in numbers:
        total_sum += number
        if total_sum > n:
            return total_sum
