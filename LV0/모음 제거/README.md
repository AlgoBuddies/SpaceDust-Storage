list 문자열 비교 관련해서 공부하고 이곳에 정리하기
commit : https://github.com/AlgoBuddies/SpaceDust-Storage/commit/b689321f3dea6e66d1fcdc4c5ca38b71ed10b9d9

참고 사이트 :
https://cheris8.github.io/python/PY-Compare-String/
https://engineer-mole.tistory.com/238
https://velog.io/@yoonji/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4LV.0%EB%AA%A8%EC%9D%8C-%EC%A0%9C%EA%B1%B0

---

## 파이썬 문법

### join의 사용

해당 문제의 경우 모음을 제거한 문자를 list 형태로 저장, 그 형태를 join을 이용하여 하나의 문자열로 합치는 과정을 이용하여 해결할 수 있다.

```
"".join(리스트)
"구분자".join(리스트)
```

위의 두 방법으로 join을 사용할 수 있다.

---

## join을 이용한 리스트 -> 문자열

```
a = "".join(n)
print(a)
```

## 반복문을 이용한 리스트 -> 문자열

```
a = ''
for i in n:
    a += i

print(a)
```
