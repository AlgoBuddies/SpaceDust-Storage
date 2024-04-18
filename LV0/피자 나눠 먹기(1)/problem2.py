n = 15  # 코드 테스트를 위해 추가한 임의의 숫자

def solution(n):
    answer = 0
    if n > 7:
        answer = n // 7
        if n % 7 >= 1:
            answer += 1
    else:
        answer = 1
    return answer

print(solution(n))  # 코드 테스트를 위해 추가한 print문