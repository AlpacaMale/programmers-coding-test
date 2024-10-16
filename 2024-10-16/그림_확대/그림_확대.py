def solution(picture, k):
    new_picture = []
    for string in picture:
        line = "".join(char * k for char in string)
        for _ in range(k):
            new_picture.append(line)
    return new_picture
