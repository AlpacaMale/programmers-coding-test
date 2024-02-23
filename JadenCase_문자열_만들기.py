def solution(s):
    to_jaden_case = True
    result = ''
    for char in s:
        if to_jaden_case:
            result+=char.upper()
            to_jaden_case=False
        else:
            result+=char.lower()
        if char == ' ':
            to_jaden_case = True
    return result

#내장함수가 더 빠르다
def solution(s):
    return ' '.join(word.lower().capitalize() for word in s.split(' '))
