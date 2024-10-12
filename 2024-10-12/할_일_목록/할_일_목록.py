def solution(todo_list, finished):
    return [todo for todo, is_finished in zip(todo_list, finished) if not is_finished]
