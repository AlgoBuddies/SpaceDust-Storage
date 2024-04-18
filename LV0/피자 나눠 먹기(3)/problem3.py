n = 10  # 코드 테스트를 위해 추가한 임의의 숫자 1
slice = 7   # 코드 테스트를 위해 추가한 임의의 숫자 2

def solution(slice, n):
    answer = 0
    if n > slice:
        answer = n // slice
        if n % slice >= 1:
            answer += 1
    else:
        answer = 1
    return answer

print(solution(slice, n))  # 코드 테스트를 위해 추가한 print문