from collections import Counter
from math import prod


def get_counter(number):
    counter = 2
    array = []
    while number != 1:
        if number % counter == 0:
            number //= counter
            array.append(counter)
        else:
            counter += 1
    return Counter(array)


def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom2 * denom1
    numer_counter = get_counter(numer)
    denom_counter = get_counter(denom)
    divide = prod((numer_counter & denom_counter).elements())
    return [numer // divide, denom // divide]
