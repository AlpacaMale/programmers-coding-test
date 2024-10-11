def solution(n, m, section):
    for index, area in enumerate(section):
        while index + 1 < len(section) and section[index + 1] < area + m:
            section.pop(index + 1)
    return len(section)