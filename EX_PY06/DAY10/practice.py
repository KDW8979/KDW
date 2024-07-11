# 오늘의 운세
import random
def fortune():
    choice=random.choice(['대길 ㅋㅋㅋ','길','소길','말길','흉 ','대흉 ㅡㅡ'])
    return choice

print(f'오늘의 점괘 : {fortune()}')

