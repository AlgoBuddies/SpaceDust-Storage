def solution(n):
    answer = 0
    x = 1
    while answer != 1:
        answer = n % x
        x += 1
    return x - 1