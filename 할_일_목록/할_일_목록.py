def solution(todo_list, finished):
    return [todo for todo, isfinished in zip(todo_list, finished) if not isfinished]