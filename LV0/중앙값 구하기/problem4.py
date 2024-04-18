array = [1, 2, 7, 10, 11]  # 코드 테스트를 위해 추가한 임의의 숫자

def solution(array):
    array.sort()
    return array[len(array) // 2]

print(solution(array))  # 코드 테스트를 위해 추가한 print문