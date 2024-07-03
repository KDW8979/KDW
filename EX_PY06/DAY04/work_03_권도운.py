# p.143
lux={'health':490, 'mana':334, 'melee':55, 'armor':18.72}

# p.144
lux={'health':490, 'health':800, 'mana':334, 'melee':55, 'armor':18.72}
print(lux['health'])

x={100: 'hundred', False:0,3.5:[3.5,3.5]}
print(x)

# x={[10,20]:100} 
# x={{'a':10}:100}  ==> 키에는 리스트와 딕셔너리를 사용할 수 없습니다

# p.145
x={}
y=dict()
print(x); print(y)

lux1=dict(health=490, mana=334, melee=550, armor=18.72)
print(lux1)

lux2=dict(zip(['health','mana','melee','armor'],[490,334,550,18.72]))
print(lux2)

lux3=dict([('health',490),('mana',334),('melee',550),('armor',18.72)])
print(lux3)

# p.146
lux4=dict({'health':490, 'mana':334, 'melee':550, 'armor':18.72})
print(lux4)

lux={'health':490, 'mana':334, 'melee':55, 'armor':18.72}
print(lux['health']); print(lux['armor'])

lux={'health':490, 'mana':334, 'melee':55, 'armor':18.72}
lux['health']=2037
lux['mana']=1184
print(lux)

# p.147
lux['mana_regen'] = 3.28
print(lux)

lux={'health':490, 'mana':334, 'melee':55, 'armor':18.72}
# print(lux['attack_speed']) => 키가 없음

lux={'health':490, 'mana':334, 'melee':55, 'armor':18.72}
print('health' in lux)
print('attack_speed' in lux)

print('health' not in lux)
print('attack_speed' not in lux)

# p.148
lux={'health':490, 'mana':334, 'melee':55, 'armor':18.72}
print(len(lux))
print(len({'health':490, 'mana':334, 'melee':55, 'armor':18.72}))

# 12.4 연습문제
camile={'health':575.6, 'health_regen':7, 'mana':338.8, 'mana_regen':1.63, 'melee':125, 'attack_damage':60, 'attack_speed':0.625, 'armor':26, 'magic_resistance':32.1, 'movement_speed':340}

print(camile['health'])
print(camile['movement_speed'])

# 12.5 심사문제

# x=input().split()
# y=input().split()
# z=dict(zip(x,y))
# print(z)

keys=input('게임 능력라벨 입력(예: health, health_regen): ').split()
print(f'keys => {keys}')

values=input('게임 능력치 입력(예: 575.6 1.7): ').split()
print(f'keys => {values}')

# '능력치' ==> 실수타입 형변환
values=list(map(float,values))
print(f'values => {values}')

result=zip(keys, values)
print(f'result => {result}')

# p.159
x=10
if x==10:
    pass   # 나중에 할 일을 주석으로 남겨놓기도 한다

# p.160
x=10
if x==10:
    print('x에 들어있는 숫자는')
    print('10입니다.')

x=10
if x==10:
    print('x에 들어있는 숫자는')
print('10입니다.')

x=5
if x==10:
    print('x에 들어있는 숫자는')
print('10입니다.')

# p.161
x=5
if x==10:
    print('x에 들어있는 숫자는')

print('10입니다.')


x=15

if x>=10:
    print('10이상입니다.')
    if x==15:
        print('15입니다.')
    if x==20:
        print('20입니다.')

# p. 162
if x>=10:
    print('10이상입니다.')
    if x==15:
        print('15입니다.')
    if x==20:
        print('20입니다.')


# p.163
# x=int(input())

# if x==10:
#     print('10입니다.')
# if x==20:
#     print('20입니다.')

# 13.6 연습문제

x=5
if x!=10:
    print('ok') 

# 13.7 심사문제
# price=27000
# coupon='Cash'+str(input())
# if coupon=='Cash3000' :
#     print(price-int(coupon[-4:]))

# price=72000
# coupon='Cash'+str(input())
# if coupon=='Cash5000' :
#     print(price-int(coupon[-4:]))

# p.167
x=5
if x==10:
    print('10입니다.')
else:
    print('10이 아닙니다.')

if x==10:
    print('10입니다.')
else:
    print('x에 들어있는 숫자는')
    print('10이 아닙니다.')    

# p.169
x=10

if x==10:
    print('10입니다.')
else:
    print('x에 들어있는 숫자는')

print('10이 아닙니다.')   


if True:
    print('참')
else:
    print('거짓')

if False:
    print('참')
else:
    print('거짓')

if None:
    print('참')
else:
    print('거짓')  

# p.170
if 0:
    print('참')
else:
    print('거짓') 

if 1:
    print('참')
else:
    print('거짓') 

if 0x1F:
    print('참')
else:
    print('거짓') 

if 0b1000:
    print('참')
else:
    print('거짓')

if 13.5:
    print('참')
else:
    print('거짓') 

if 'Hello':
    print('참')
else:
    print('거짓')   

if '':
    print('참')
else:
    print('거짓')      

# p.171
if not 0:
    print('참')
else:
    print('거짓') 

if not None:
    print('참')
else:
    print('거짓')     

if not '':
    print('참')
else:
    print('거짓') 

# p.172
x=10
y=20

if x==10 and y==20:
    print('참')
else:
    print('거짓')

if x>0 and x<20:
    print('20보다 작은 양수입니다.')

if 0<x<20:
    print('20보다 작은 양수입니다.')

# 14.6 연습문제
written_test=75
coding_test=True

if written_test>=80 and coding_test==True:
    print('합격')
else:
    print('불합격')

#14.7 심사문제

# score=input().split()
# score=list(map(int,score))
# average=sum(score)/len(score)
# if score[0]>=0 and score[0]<=100 and score[1]>=0 and score[1]<=100 and score[2]>=0 and score[2]<=100 and score[3]>=0 and score[3]<=100:

#     if average>=80:
#         print('합격')
#     else:
#         print('불합격')
# else:
#     print('잘못된 점수')

# (1) 4과목 점수 입력 받기           => input().split() =>[str,str,str]
# (2) 4과목 점수 모두 0~100 검사     => 
# (3) 4과목 점수 모두 0~100점 범위안에 있으면 합격/불합격 검사
# nums=['10']
# print(0<=int(nums[0])<=100)
# print(int(nums[0]) in range(101))
# [1] str 점수 4개 리스트
jumsu=input().split()

# [2] str점수 ==> int 점수 형변환
jumsu=list(map(int,jumsu))

# [3] 4과목의 점수를 0이상 100이하 범위 검사
if (0<=int(jumsu[0])<=100) and (0<=int(jumsu[1])<=100) and (0<=int(jumsu[2])<=100) and (0<=int(jumsu[3])<=100):
    # 평균 = 합계/4
    if sum(jumsu)/len(jumsu)>=80:
        print('합격')
    else:
        print('불합격')
else:
    print('잘못된 점수')

# p.177
x=20
if x==10:
    print('10입니다.')
elif x==20:
    print('20입니다.')

# p.178
x=30
if x==10:
   print('10입니다.')
elif x==20:
    print('20입니다.')  
else:
    print('10도 20도 아닙니다.')

button=int(input())


if button==1:
    print('콜라')
elif button==2:
    print('사이다')
elif button==3:
    print('환타')
else:
    print('제공하지 않는 메뉴')        

#15.3 연습문제
x=int(input())

if 11<=x<=20:
    print('11~20')
elif 21<=x<=30:
    print('21~30')
else:
    print('아무것도 해당하지 않음') 

#15.4 심사문제
age=int(input())
balance=9000

if 7<=age<=12:
    balance=balance-650
elif 13<=age<=18:
    balance=balance-1050
elif age>=19:
    balance=balance-250
 

print(balance)

