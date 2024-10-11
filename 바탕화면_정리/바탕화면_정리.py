def solution(wallpaper):
    drag = [52, 52, -1, -1]
    for row, string in enumerate(wallpaper):
        lindex = string.find("#")
        rindex = string.rfind("#")
        if lindex != -1:
            drag[0] = min(drag[0], row)
            drag[1] = min(drag[1], lindex)
            drag[2] = max(drag[2], row + 1)
            drag[3] = max(drag[3], rindex + 1)
    return drag
