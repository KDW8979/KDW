##----------------------------------------------------------
## ==> 1줄로 조건식을 축약 : 조건부표현식
##----------------------------------------------------------
## [실습] 임의의 숫자가 5의 배수인지 아닌지 결과를 출력하세요.
##        단, 2와 5를 제외한 나머지는 고려하지 X

# num=int(input())

# print('5의 배수 아님') if num%5 else print('5의 배수')
# print('5의 배수') if not num%5 else print('5의 배수 아님')

## [실습] 문자열을 입력 받아서 문자열의 원소 개수를 저장
## - 단 원소 개수가 0이면 None 저장
## - (1) 입력받기 input()
## - (2) 원소/요소 개수 파악 len()
## - (3) 원소/요소 개수 저장 단, 0인 경우 None 저장하기

# data=input()
# # result=len(data)
# if len(data):
#     result=len(data)
# else:
#     result=None

# result=len(data) if len(data) else None
# print(f'{data}의 원소/요소 개수: {result}개')

## [실습] 연산자(4칙연산자 : +,-,*,/)와 숫자 2개 입력 받기
## - 입력된 연산자에 따라 계산 결과 저장
## - 예) 입력 : + 10 3   출력 : 13
command=input('4칙연산자 1개와 숫자 2개 입력\n(예: + 10 3) :').split()

print(command)
# ['+', '5', '9']
command[1]=int(command[1])
command[2]=int(command[2])
if command[0]=='+':
    result=command[1] + command[2]
elif command[0]=='-':
    result=command[1] - command[2]
elif command[0]=='*':
    result=command[1] * command[2] 
elif command[0]=='/':
    result=command[1] / command[2]
else:
    print('4칙 연산자가 아닙니다.')


