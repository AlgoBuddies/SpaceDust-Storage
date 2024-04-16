n = 10  # 코드 테스트를 위해 추가한 임의의 숫자

def solution(n):
    answer = []
    
    for i in range(n+1):
        if i % 2 == 1:
            answer.append(i)
    return answer

print(solution(n))  # 코드 테스트를 위해 추가한 print문