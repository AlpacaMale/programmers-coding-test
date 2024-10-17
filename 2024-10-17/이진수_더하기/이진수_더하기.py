def solution(bin1, bin2):
    result = int(bin1, 2) + int(bin2, 2)
    return bin(result)[2:]
