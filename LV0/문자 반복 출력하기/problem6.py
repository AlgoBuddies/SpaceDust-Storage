def solution(my_string, n):
    answer = ''
    for i in range(len(my_string)):
        answer = answer + my_string[i] * n
    return answer

# 처음에 생각한 방법
# def solution(my_string, n):
#     answer = ''
#     for i in range(len(my_string)):
#         for j in range(0, n):
#             answer = answer + my_string[i]
#     return answer