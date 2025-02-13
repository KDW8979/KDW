# -----------------------------------------------------------------------------
# 사용자 정의 함수
# -----------------------------------------------------------------------------
# 덧셈, 뺄셈, 곱셈, 나눗셈 함수를 각각 만들기
# - 매개변수 : 정수 2개, num1, num2
# - 함수결과 : 연산 결과 반환
#-----------------------------------------------------------------------------
def add(num1,num2):
    return num1+num2


def minus(num1,num2):
    return num1-num2


def mul(num1,num2):
    return num1 * num2
 


def div(num1,num2):
    return num1/num2 if num2 else '0으로 나눌 수 없음' 

# -----------------------------------------------------------------------------
#  함수 기능 : 입력 데이터가 유효한 데이터인지 검사해주는 기능
# 함수 이름 : check_data
# 매개 변수 : 문자열 데이터, 데이터 갯수 data, count,sep=' '
# 함수 결과 : 유효 여부 True/False
# -----------------------------------------------------------------------------
def check_data(data, count, sep=' '):
    # 데이터 여부
    if len(data):
        # 데이터 분리 후 갯수 체크
        data2=data.split(sep)
        if count == len(data2):
            return True
        else:
            return False
    else:
        return False    

print(check_data('+ 1 3', 3))
print(check_data('+ 1 3', 3,','))



# 함수 사용하기 즉, 호출--------------------------------------
# [실습] 사용자로부터 연산자, 숫자1, 숫자2를 입력받아서
#        연산 결과를 출력해주세요.
# - input("연산자, 숫자1, 숫자2 : ").split(',')
op,num1,num2=input('연산자, 숫자1, 숫자2 : ').split()
print(op,num1,num2)

if op not in ['+','-','*','/']:
    print(f'{op} 잘못된 연산자입니다.')
else:
    if num1.isdecimal() and num2.isdecimal():
        num1=int(num1)
        num2=int(num2)
        result=0
        if op=='+':
            result=add(num1,num2)
        elif op=='-':
            result=minus(num1,num2)
        elif op=='*':
            result=mul(num1,num2)
        else:
            result=div(num1,num2)
        print(f'{num1}{op}{num2}={result}')    
    else:
        print('정수만 입력 가능합니다.')


# def calculate(data):
#     num1=int(num1)
#     num2=int(num2)
#     if data[0]=='+':
#         print(add(num1,num2))
#     elif data[0]=='-':
#         print(minus(num1,num2))
#     elif data[0]=='*':
#         print(mul(num1,num2))
#     else:
#         print(div(num1,num2))            
