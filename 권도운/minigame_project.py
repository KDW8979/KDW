import random
            
# 내가 낼 거 정하기                        
def get_user_choice():
    user_choice=input('\n가위바위보 게임에 오신 것을 환영합니다.\n\n가위, 바위, 보 중 하나를 입력해주세요 : ')
    while user_choice not in ['가위','바위','보']:
        print('\n가위, 바위, 보 중 하나만 입력할 수 있습니다.')
        user_choice=input('\n가위, 바위, 보 중 하나를 입력해주세요 : ')
    return user_choice   
 
# 컴퓨터가 낼 거 정하기
def get_com_choice():
    choice=random.choice(['가위','바위','보'])
    return choice


# 누가 이기는지 정하기
def winner(user_choice,com_choice):
    if user_choice==com_choice:
        print('\nDraw!')
    elif (user_choice=='가위' and com_choice=='바위') or (user_choice=='바위' and com_choice=='보') or (user_choice=='보' and com_choice=='가위'):
        print('\nYou Lose!')
    else:
        print('\nYou Win!')     

# 다시 할지 물어보기
def ask_play_again():
    while True:
        play_again = input('\n다시 하시겠습니까? (예/아니오): ')
        if play_again in ['예', '아니오']:
            return play_again
        else:
            print('\n예/아니오로 대답하십시오.')

# 가위바위보 게임 플레이
def play_game():
    while True:
        user_choice=get_user_choice()
        com_choice=get_com_choice()
        print(f'\n당신의 선택 : {user_choice}')
        print(f'컴퓨터의 선택 : {com_choice}')
        result=winner(user_choice,com_choice)
        play_again = ask_play_again()
        if play_again == '아니오':
            break
        elif play_again == '예':
            continue

# 점괘뽑기

def get_fortune():
    fortunes=['대길','길','소길','말길','흉','대흉']
    print(f'\n당신의 점괘는 *{random.choice(fortunes)}*입니다.')
    
        

# 숫자찾기 게임
def num_game():
    number = random.randint(1, 100)
    attempt = 10
    print('\n숫자게임은 1~100 사이의 숫자 중 컴퓨터가 임의로 정한 숫자를 맞추는 게임입니다.\n10번 안에 컴퓨터가 정한 숫자를 맞춰보세요.')
    while attempt > 0:
        
        user_input = input('\n1~100까지의 숫자 중 하나를 입력하세요 : ').strip()  
        if not user_input.isdigit():
            print('\n1에서 100 사이의 숫자를 입력해주세요.')
            continue
        user_input=int(user_input)        
        if not (1 <= user_input <= 100):
            print('\n1에서 100 사이의 숫자를 입력해주세요.')
            continue
        elif user_input == '':
            print('\n1에서 100 사이의 숫자를 입력해주세요.')
            continue
        
        if number > user_input:
            attempt -= 1
            print(f'{user_input}보다 큽니다. 남은 기회: {attempt}')
        elif number < user_input:
            attempt -= 1
            print(f'{user_input}보다 작습니다. 남은 기회: {attempt}')
        else:
            print('정답입니다!')
            break
    
    if attempt == 0:
        print(f'Game Over. 정답은 {number}입니다.')
    
    play_again = ask_play_again()
    if play_again == '예':
        num_game()
    else:
        print('게임을 종료합니다.')




# 메인화면
def print_menu():
    print(f'{"-":-^20}')
    print(f'{"허접한 미니게임천국":<20}')
    print(f'{"-":-^20}')
    print(f'{" 1.  가위바위보 ":20}')
    print(f'{" 2.  숫자찾기 ":20}')
    print(f'{" 3.  점괘뽑기 ":20}')
    print(f'{" 4.  종    료 ":20}')
    print(f'{"-":-^20}')

# 선택문
while True:
    print_menu()
    choice=input("\n메뉴를 선택해주세요 : ")
    if choice.isdecimal():
       choice=int(choice)
       if not 1<=choice<=4:
           print("\n지원하지 않는 메뉴입니다.")    
    else:
        print("\n지원하지 않는 메뉴입니다.")    


    # 종료하기    
    if choice==4:
        print('\n프로그램을 종료합니다.')
        break
    # 숫자찾기
    elif choice==2:
        num_game()
    # 점괘뽑기
    elif choice==3:
        print('\n오늘의 점괘를 뽑아봅시다. 점괘는 대길,길,소길,말길,흉,대흉이 있습니다.')
        input('엔터를 누르면 점괘를 뽑습니다.')
        get_fortune()
    # 가위바위보   
    elif choice==1:
        play_game()



             





