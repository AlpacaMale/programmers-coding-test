def solution(a, b):
    # 날짜 정보를 두개의 딕셔너리에 기입한 후 맞게 연산
    day = {3: "SUN", 4: "MON", 5: "TUE", 6: "WED", 0: "THU", 1: "FRI", 2: "SAT"}
    month_per_day = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    day_after = sum(month_per_day[month] for month in range(1, a)) + b
    return day[(day_after) % 7]
