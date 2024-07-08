# -----------------------------------------------------------------------------
# 함수(Fuction) 이해 및 활용
# 함수기반 계산기 프로그램
# - 4칙 연산 기능별 함수 생성 => 덧셈, 뺄셈, 곱셈, 나눗셈
#- 2개 정수만 계산
# -----------------------------------------------------------------------------

# def calc(num1,op,num2):
#     if op=='+':
#         result=num1+num2
#     elif op=='-':
#         result=num1-num2
#     elif op=='*':
#         result=num1*num2
#     elif op=='/':
#         if num2:
#             result=num1/num2
#         else:
#             result='0으로 나눌 수 없습니다.'
#     return result

# print(calc(2,'/',0))

## 계산기 프로그램-----------------------------------------------------------------
# - 사용자가 종료를 원할때 종료 => 'x', 'X' 입력 시
# - 연산방식과 숫자 데이터 입력 받기
# -----------------------------------------------------------------------------
def add(num1,num2):
    result= (num1+num2)
    return result

def sub(num1,num2):
    result =(num1-num2)
    return result

def mul(num1,num2):
    result=num1*num2
    return result

def div(num1,num2):
    if num2:
        result=num1/num2
    else:
        result=None 
    return result



while True:
    # (1) 입력 받기
    req=input('연산(+,-,*,/)방식과 정수 2개 입력(예: + 10 2)')
    # (2) 종료 조건 검사
    if req=='x' or req=='X':
        print('계산기를 종료합니다.')
        break
    # (3) 입력에 연산방시과 데이터 추출
    op, num1, num2 = req.split()  # ['+', '10','2']
    # str 정수 ==> int 변환
    num1=int(num1)
    num2=int(num2)
    # 연산방식에 따라서 계산 진행
    if op=='+':
        print(f'{num1}+{num2}={add(num1,num2)}')
    elif op=='-':
        print(f'{num1}+{num2}={sub(num1,num2)}')
    elif op=='*':
        print(f'{num1}+{num2}={mul(num1,num2)}') 
    elif op=='/':
        print(f'{num1}+{num2}={div(num1,num2)}')          

