def solution(n, k):
    answer = 0
    if n / 10 > 0 and k > 0:
        n = (n * 12000) - (2000 * (n // 10))
        answer = n + k * 2000
    return answer