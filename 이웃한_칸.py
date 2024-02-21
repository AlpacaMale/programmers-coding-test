def solution(s, skip, index):
    alphabet = sorted(set("abcdefghijklmnopqrstuvwxyz") - set(skip))
    length = len(alphabet)
    s_shift = []
    for char in s:
        offset = alphabet.index(char) + index
        s_shift.append(alphabet[offset % length])
    return "".join(s_shift)
