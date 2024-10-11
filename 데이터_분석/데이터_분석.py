def solution(data, ext, val_ext, sort_by):
    table = [
        {"code": code, "date": date, "maximum": maximum, "remain": remain}
        for code, date, maximum, remain in data
    ]
    for row in table[:]:
        if row[ext] >= val_ext:
            table.remove(row)
    sorted_table = sorted(table, key=lambda x: x[sort_by])
    return [list(row.values()) for row in sorted_table]
