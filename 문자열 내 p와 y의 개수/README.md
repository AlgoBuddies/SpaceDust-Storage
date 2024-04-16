[](https://school.programmers.co.kr/learn/courses/30/lessons/12916)

## 문제

```jsx
대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

[제한사항]

- 문자열 s의 길이 : 50 이하의 자연수
- 문자열 s는 알파벳으로만 이루어져 있습니다.
```

## 문제 속 조건

1. 문자열 s
2. s에서 ‘p’와 ‘y’의 개수를 비교하고 이를 boolean 값으로!
1 ) p = y : True
2 ) p =! y : False
3 ) p, y = O : True
3. 대소문자 구분 안함

## 글로 적어보는 알고리즘

1. 문자열을 받아온다
2. 문자열에 p가 있는지 확인
3. p가 있다면 ++
4. 문자열에 y가 있는지 확인
5. y가 있다면 ++
6. p와 y의 크기를 비교
7. p가 크거나 y가 큰 경우 False
8. 그 외의 경우 True

## 코드

```jsx
def solution(s):
    p = 0
    y = 0
    for i in range(len(s)):
        if s[i] == 'p':
            p += 1
        elif s[i] == 'y':
            y += 1
    
    if p > y or p < y:
        return False
    else:
        return True
```

문제점 : 코드를 실행하였을 떄 작동은 한다. 하지만 최종 제출 시 오답 처리가 몇 개 발생

이유를 찾아보자.

조건을 확인해보자.

조건 1 : 문자열 s (s를 받아오고 그것이 출력되는 것도 확인함)

조건 2 : s에서 ‘p’와 ‘y’의 개수를 비교하고 이를 boolean 값으로!(이것도 일부 테스트케이스에서 성공이 뜨고 있다. if문 확인 시 문제 없음)

조건 3 : 대소문자 구분 안함(따로 코드에서 대소문자 관련해서 걸어준게 없긴하다..?)

일단 조건을 하나씩 넘겨보면 조건 3을 누락해서 생기는 문제인 것 같다.

그렇다면 python에서 대소문자 구분은 어떻게 처리할 수 있는가?

```jsx
def solution(s):
    p = 0
    y = 0
    for i in range(len(s)):
        if s[i] == 'p' or 'P':
            p += 1
        elif s[i] == 'y' or 'Y':
            y += 1
    
    if p > y or p < y:
        return False
    else:
        return True
```

코드를 이렇게 바꾸었는데도 결과가 같았다. 그 말은 즉슨 추가한 대문자 P, Y에 대한 비교가 제대로 이루어지지 않고 있다는 뜻

```jsx
def solution(s):
    p = 0
    y = 0
    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P':
            p += 1
        elif s[i] == 'y' or s[i] == 'Y':
            y += 1
    
    if p > y or p < y:
        return False
    else:
        return True
```

이런식으로 코드를 바꾸니 해결이 되었다.