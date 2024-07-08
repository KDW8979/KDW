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
# -----------------------------------------------------------------------------
# 함수 기능: 계산기 메뉴를 출력하는 함수
# 함수 이름: print_menu
# 매개 변수: 없음
# 함수 결과: 없음
# -----------------------------------------------------------------------------


def print_menu():
    print(f'{"*":*^16}')
    print(f'{"계 산 기":^16}')
    print(f'{"*":*^16}')
    print(f'{"* 1  덧      셈 *":16}')
    print(f'{"* 2  뺄      셈 *":16}')
    print(f'{"* 3  곱      셈 *":16}')
    print(f'{"* 4  나  눗  셈 *":16}')
    print(f'{"* 5  종      료 *":16}')
    print(f'{"*":*^16}')



# print(f'{"*":*^16}')  # 가운데 정렬
# print(f'{"*":->16}')  # 오른쪽 정렬
# print(f'{"*":;<16}')  # 왼쪽 정렬


# -----------------------------------------------------------------------------
# 함수 기능: 연산 수행 후 결과를 반환하는 함수
# 함수 이름: calc
# 매개 변수: 함수명(add, sub, mul, div)
# 함수 결과: 없음
# -----------------------------------------------------------------------------


def calc(func, op):
#   num1, num2 = input('정수 2개(예: 10 2)').split()
#   num1=int(num1)
#   num2=int(num2)
    data=input("정수 2개(예: 10 2)")
    if check_data(data,2):
        data=data.split()
        print(f'결과: {data[0]}{op}{data[1]}={func(int(data[0]), int(data[1]))}')
    else:
        print(f"{data} : 올바른 데이터가 아닙니다.")
    

    print(f'결과: {num1}{op}{num2}={func(num1,num2)}')

# -----------------------------------------------------------------------------
# 함수 기능: 입력받은 데이터가 유효한 데이터인지 검사하는 함수
# 함수 이름: check_data
# 매개 변수: str 데이터(예: '10,3), 데이터 수
# 함수 결과: True 또는 False
# -----------------------------------------------------------------------------
def check_data(data,count):
    # 입력된 str ===> List 변환 : split()
    data=data.split()
    #갯수 체크
    
    if len(data)==count:
        # 0~9로 구성된 str 체크
        isOk=True
        for d in data:
            if not d.isdecimal():
                isOk=False
                break
        return isOk
    else:
        return False

## 계산기 프로그램 -----------------------------------------------------------------------------
# - 사용자에게 원하는 계산을 선택하는 메뉴 출력
# - 종료 메뉴 선택 시 프로그램 종료
# => 반복 ---> 무한반복 : while
# -----------------------------------------------------------------------------
# 메뉴 출력

while True:
    # 메뉴 출력
    print_menu()

    # 메뉴 선택 요청
    choice=input("메뉴 선택: ")
    if choice.isdecimal():
       choice=int(choice)
        
    else:
        print("0~9사이 숫자만 입력하세요")    
        continue
        
    # 종료 조건(5번 메뉴 선택) 처리
    if choice==5:
        print("프로그램을 종료합니다.")
        break
    
    elif choice==1:   #덧셈
        print("덧셈")
        calc(add, '+')
    elif choice==2:   #뺄셈
        print("뺄셈")
        calc(sub, '-')
    elif choice==3:   #곱셈
        print("곱셈")
        calc(mul, '*')
    elif choice==4:   #나눗셈
        print("나눗셈")
        calc(div, '/')
    else:
        print("선택된 메뉴는 없습니다.")

