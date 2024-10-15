def solution(arr):
    count = -1
    while len(arr) != 0:
        new_arr = []
        for number in arr:
            if number >= 50 and number % 2 == 0:
                new_arr.append(number / 2)
            elif number < 50 and number % 2 == 1:
                new_arr.append(number * 2 + 1)
        arr = new_arr
        count += 1
    return count
