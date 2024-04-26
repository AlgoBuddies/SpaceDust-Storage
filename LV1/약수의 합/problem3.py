def solution(n):
    answer = 0
    for i in range(n - n + 1, n + 1):
        if n % i == 0:
            answer = answer + i
    return answer