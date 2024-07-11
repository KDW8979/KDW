# 숫자 맞추기 게임
import random



def num_game():
    number = random.randint(1, 100)
    attempt = 10
    
    while attempt > 0:
        user_input = input('1~100까지의 숫자 중 하나를 입력하세요 : ').strip()
        user_number = int(user_input)
        if not (1 <= user_number <= 100):
            print('1에서 100 사이의 숫자를 입력해주세요.')
            continue
        
        if user_input == '':
            print('입력이 없습니다. 숫자를 입력해주세요.')
            continue
        
        
            
        
        
        if number > user_number:
            attempt -= 1
            print(f'{user_number}보다 큽니다. 남은 기회: {attempt}')
        elif number < user_number:
            attempt -= 1
            print(f'{user_number}보다 작습니다. 남은 기회: {attempt}')
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

num_game()