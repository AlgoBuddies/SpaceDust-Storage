def solution(hp):
    answer = 0
    while hp != 0:
        if hp >= 5:
            answer = answer + hp // 5
            hp = hp - (hp // 5) * 5
        elif hp >= 3:
            answer = answer + hp // 3
            hp = hp - (hp // 3) * 3
        elif hp >= 1:
            answer = answer + hp // 1
            hp = hp - (hp // 1) * 1
            
    return answer