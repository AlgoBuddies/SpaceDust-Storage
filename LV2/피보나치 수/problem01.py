def solution(n):
    answer = 0
    
    x = max(0, n - 2)
    y = max(0, n - 1)
    
    if x == 1 or n == 1:
        answer += 1
    elif x == 0 or n == 0:
        answer += 0
    else:
        answer += x
    if y == 1 or n == 1:
        answer += 1
    elif y == 0 or n == 0:
        answer += 0
    else:
        answer += y
    
    return answer

print(solution(3))


# def solution(n):
#     answer = 0
    
#     # max(0, n)을 하면 0 이하의 음수는 전부 0으로 취급하여 변수에 저장
#     x = max(0, n - 2)
#     y = max(0, n - 1)
    
#     if x == 0:
#         answer += 0
#     elif x == 1:
#         answer += 1
#     else:
#         asnwer = answer + x - 1
    
#     if y == 0:
#         answer += 0
#     elif y == 1:
#         answer += 1
#     else:
#         asnwer = answer + y - 1
    
#     return answer