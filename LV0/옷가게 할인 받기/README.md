소수점 이하 버리는 문법 까먹어서 여러 방법 시도해봄
int로 덮는다 -> int의 경우 반올림 되어버려서 안됨

처음에는 int를
``` price = price - int(price * (20 / 100)) ```
로 사용했는데 이 방법에서
``` price = price - price * (20 / 100) 
return int(price) ```

로 수정하니 소수점 삭제가 아닌 반올림이 되는 문제를 해결할 수 있었다.