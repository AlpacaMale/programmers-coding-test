def solution(numbers):
    result = []
    for first in range(len(numbers)):
        for second in range(first + 1, len(numbers)):
            result += [numbers[first] + numbers[second]]
    return sorted(set(result))
