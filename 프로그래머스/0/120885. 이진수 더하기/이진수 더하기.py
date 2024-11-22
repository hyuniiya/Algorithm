def solution(bin1, bin2):
    total = int(bin1, 2) + int(bin2, 2)
    return bin(total)[2:]