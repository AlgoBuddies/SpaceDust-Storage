# 0단계 문제

def solution(box, n):
    answer = 0
    
    a = box[0] // n
    b = box[1] // n
    c = box[2] // n
    answer = a * b * c
    
    return answer

# 주사위 넓이랑 상자 넓이 비교 + 가로 세로 높이 길이 비교해서 주사위 몇개 들어가는지 return하며 될 듯!