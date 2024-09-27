'''
1번 문제) x만큼 간격이 있는 n개의 숫자

함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개
지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수,
solution을 완성해주세요.

제한 조건
● x는-10000000 이상, 10000000 이하인 정수입니다.
● n은 1000 이하인 자연수입니다.
'''

def solution(x: int, n: int):
    if not (-10000000 <= x <= 10000000):
        raise ValueError("x는-10000000 이상, 10000000 이하인 정수입니다.")
    if not (1 <= n <= 1000):
        raise ValueError("n은 1000 이하인 자연수입니다.")
    
    return [x * i for i in range(1, n + 1)]

try:
    solution(10000001, 5)
except ValueError as e:
    print(e)
    
try:
    solution(5, 1001)
except ValueError as e:
    print(e)


print(solution(2, 10))