시간 두고 계속 풀어볼 문제
이건 풀어야지!
접근 방식을 이상하게 접근한건가? 내가 피보나치 수를 제대로 이해하지 않은건가?

내 기억상 F(n) = F(n-1) + F(n-2)
이런식으로 공식이 흘러가는데 이걸 재귀함수로 처리했던 기억이 있는데
이 방법도 한 번 떠올려봐야겠다.

```
def solution(n)
  solution(n-1)
  soultion(n-2)
```

방법은 둘째치고 그냥 위에 코드처럼 흘러가는? 그런 재귀

---

### 이전 접근 코드

```
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
```
