def solution(lines):
    numbers = set()
    result = 0
    for start, end in lines:
        for number in range(start, end + 1):
            numbers.add(number)

    for number in numbers:
        count = 0
        for start, end in lines:
            if start <= number <= end and start <= number + 1 <= end:
                count += 1
        if count >= 2:
            result += 1
    return result
