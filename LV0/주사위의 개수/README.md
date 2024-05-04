중간에 임시 코드

```

def solution(box, n):
    answer = 0
    v = n

    if box[0] >= n or box[1] >= n or box[2] >= n:
        answer = n / v
    else:
        n += n
    return answer

# 주사위 넓이랑 상자 넓이 비교 + 가로 세로 높이 길이 비교해서 주사위 몇개 들어가는지 return하며 될 듯!

```

위에 코드에 반복 조건만 걸어주면 완료!
좀 더 고민하고 다시 풀어봐야하는 문제
