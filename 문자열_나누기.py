def solution(s):
    decomposed_word_count = 0
    buffer = ""
    length = len(s)
    for index, char in enumerate(s):
        buffer += char
        if len(buffer) / 2 == buffer.count(buffer[0]) or index == length - 1:
            decomposed_word_count += 1
            buffer = ""
    return decomposed_word_count
