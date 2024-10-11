def solution(sizes):
    max_width, max_height = 0, 0
    for size1, size2 in sizes:
        max_width = max(max_width, max(size1, size2))
        max_height = max(max_height, min(size1, size2))
    return max_width * max_height
