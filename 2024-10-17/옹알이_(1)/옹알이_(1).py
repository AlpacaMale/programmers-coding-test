def solution(babbling):
    pronounces = ["aya", "ye", "woo", "ma"]
    count = 0
    for dada in babbling:
        for pronounce in pronounces:
            dada = dada.replace(pronounce, " ")
        if not dada.strip():
            count += 1
    return count
