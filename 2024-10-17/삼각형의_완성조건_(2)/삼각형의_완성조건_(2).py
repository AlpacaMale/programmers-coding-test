def solution(sides):
    start = max(sides) - min(sides) + 1
    end = sum(sides)
    return len(range(start, end))
