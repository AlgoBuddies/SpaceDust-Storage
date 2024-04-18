price = 100010  # 코드 테스트를 위해 추가한 임의의 숫자

def solution(price):
    if price >= 500000:
        price = price - price * (20 / 100)
    elif price >= 300000:
        price = price - price * (10 / 100)
    elif price >= 100000:
        price = price - price * (5 / 100)

    return int(price)

print(solution(price))  # 코드 테스트를 위해 추가한 print문