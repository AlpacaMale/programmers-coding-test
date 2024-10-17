from collections import Counter


def solution(spell, dic):
    spell_counter = Counter(spell)
    for word in dic:
        if len(spell_counter - Counter(word)) == 0:
            return 1
    return 2
