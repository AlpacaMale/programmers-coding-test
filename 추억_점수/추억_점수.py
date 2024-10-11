def solution(name, yearning, photos):
    # dict와 zip을 활용하여 key가 name이고 value가 yearning인 딕셔너리를 만들 수 있다
    yearning_table = dict(zip(name, yearning))
    result = []
    for photo in photos:
        result.append(
            sum(yearning_table[people] for people in photo if people in yearning_table)
        )
    return result
