import random

# def game():
#     game=['가위','바위','보']
#     com=random.choice(game)
    
#             # 바위 냈을때
#     elif a=='바위':
#             if com=='가위':
#                 print('You Win!')
#             elif com=='바위':
#                 print('무승부로 하지 않을래?')
#             elif com=='보':
#                 print('You Lose')
#             # 보 냈을때
#     elif a=='보':
#             if com=='가위':
#                 print('You Lose')
#             elif com=='바위':
#                 print('You Win!')
#             elif com=='보':
#                 print('무승부로 하지 않을래?')  
#     else:
#         print('거 장난이 너무 심한거 아니오!')                

# def print_menu():
#     print(f'{"*":*^17}')
#     print(f'{" 가위바위보 게임":<17}')
#     print(f'{"*":*^17}')
#     print(f'{" 1.  P L A Y ":17}')
#     print(f'{" 2.  How to Play ":17}')
#     print(f'{" 3.  E X I T ":17}')
#     print(f'{"*":*^17}')


# while True:
#     print_menu()
#     choice=input("메뉴를 선택하시오: ")
#     if choice.isdecimal():
#        choice=int(choice)

#     else:
#         print("지원하지 않는 기능입니다.")    


#     # 종료하기    
#     if choice==3:
#         print('플레이해주셔서 감사합니다.')
#         break
#     # 설명보기
#     elif choice==2:
#         print('컴퓨터와 가위바위보 게임을 합니다.\n가위, 바위, 보 중에 내고 싶은 것 하나를 입력하면 됩니다.\n그럼 게임을 시작하지...')
#     # 본게임    
#     elif choice==1:
#         fist=input('가위, 바위, 보 중 하나를 내시오.')    
#         game(fist)
#         if fist=='가위':
#             if =='가위':
#                 print('무승부로 하지 않을래?')
#             elif com=='바위':
#                 print('You Lose')
#             elif com=='보':
#                 print('You Win!')
            
                        
def game_user(a):
    if a!= '가위' or a!= '바위' or a!= '보': 
        print('거 장난이 너무 심한거 아니오!')
    else:    
        print('가위, 바위, 보 중 하나를 내시오. : ', input())


def game_com():
    a=random.choice['가위', '바위', '보']
    return a

def print_menu():
    print(f'{"*":*^17}')
    print(f'{" 가위바위보 게임":<17}')
    print(f'{"*":*^17}')
    print(f'{" 1.  P L A Y ":17}')
    print(f'{" 2.  How to Play ":17}')
    print(f'{" 3.  E X I T ":17}')
    print(f'{"*":*^17}')


while True:
    print_menu()
    choice=input("메뉴를 선택하시오: ")
    if choice.isdecimal():
       choice=int(choice)

    else:
        print("지원하지 않는 기능입니다.")    


    # 종료하기    
    if choice==3:
        print('플레이해주셔서 감사합니다.')
        break
    # 설명보기
    elif choice==2:
        print('컴퓨터와 가위바위보 게임을 합니다.\n가위, 바위, 보 중에 내고 싶은 것 하나를 입력하면 됩니다.\n그럼 게임을 시작하지...')
    # 본게임    
    elif choice==1:
        game_com()
        game_user()
        if game_com=='가위':
           if game_user=='가위':
               print('무승부로 하지 않을래?')
           elif game_user=='바위':
               print('You Win!')
           elif game_user=='보':
               print('You Lose!')
        elif game_com=='바위':
           if game_user=='가위':
               print('You Lose!')
           elif game_user=='바위':
               print('무승부로 하지 않을래?')
           elif game_user=='보':
               print('You Win!')
        elif game_com=='보':
           if game_user=='가위':
               print('You Win!')
           elif game_user=='바위':
               print('You Lose!')
           elif game_user=='보':
               print('You Win!')       





