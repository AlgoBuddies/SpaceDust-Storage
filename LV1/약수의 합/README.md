ZeroDivisionError: integer division or modulo by zero

해당 에러가 계속 발생해서 한 5~10분 정도 애먹은 문제
원인은 for i in range 부분에서 괄호() 안에 n을 그대로 넣어버려서 해당 문제 발생
위의 원인이 되는 부분을

for i in range(n - n + 1, n + 1):

로 수정하니 코드 정상 작동하는 것을 확인
