def solution(n, lost, reserve):
    remaining_lost = sorted(l for l in lost if not l in reserve)
    remaining_reserve = [r for r in reserve if r not in lost]
    for num in remaining_lost[:]:
        if num - 1 in remaining_reserve:
            remaining_lost.remove(num)
            remaining_reserve.remove(num - 1)
        elif num + 1 in remaining_reserve:
            remaining_lost.remove(num)
            remaining_reserve.remove(num + 1)
    return n - len(remaining_lost)
