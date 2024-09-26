'''
2번 문제) 핸드폰 번호 가리기

이브레인 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를
가립니다.
전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지
숫자를 전부*으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

제한 조건
● phone_number는 길이 4 이상, 20이하인 문자열입니다.
'''

def solution(phone_number: str):
    if not (4 <= len(phone_number) <= 20):
        raise ValueError('제한 조건에 맞지 않음')
    
    return '*' * (len(phone_number) - 4) + phone_number[-4:]

try:
    solution('123')
except ValueError as e:
    print(e) 

try:
    solution('123456789012345678901')
except ValueError as e:
    print(e) 

print(solution('4444'))
