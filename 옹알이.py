def solution(babbling):
    words = {"aya": "1", "ye": "2", "woo": "3", "ma": "4"}
    result = 0
    for blah in babbling:
        for word in words:
            blah = blah.replace(word, words[word])
        for duplication in ["11", "22", "33", "44"]:
            blah = blah.replace(duplication, "duplication")
        result += blah.isdigit()
    return result
