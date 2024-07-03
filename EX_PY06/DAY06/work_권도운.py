# p.195
i=0
while i<100:
    print('Hello, world!')
    i=i+1

# p.196
# 초기식
# while 조건식:
#      반복할 코드
#      변화식

i=0
while i<100:
     print('Hello, world!')
     i=i+1

# p.197
i=1
while i<=100:
     print('Hello, world!')
     i+=i

i=100
while i>0:
     print('Hello, world!')
     i-=1

# p.198
count=int(input('반복할 횟수를 입력하세요: '))
i=0
while i<count:
     print('Hello, world!')
     i+=1

count=int(input('반복할 횟수를 입력하세요: '))
while count>0:
     print('Hello, world!',count)
     count-=1

# p.199
import random

random.random()

random.randint(1,6)

# p.200
import random
i=0
while i !=3:
     i=random.randint(1,6)
     print(i)

dice=[1,2,3,4,5,6]
random.choice(dice)

# while True:     # while에 True를 지정하면 무한 루프
#      print('Hello, world!')

# p.201
while 1:            # 0이 아닌 숫자는 True로 취급하여 무한 루프로 동작
     print('Hello, world!')

while 'Hello':      # 내용이 있는 문자열은 True로 취급하여 무한루프로 동작
     print('Hello, world!')     

# 17.5 연습문제
i=2
j=5
while i<=32 or j>=1:
     print(i,j)
     i=i*2
     j=j-1

# 17.6 심사문제
price=int(input())
while price>=1350:
     print(price-1350)
     price=price-1350      

# p.204
i=0
while True:
     print(i)
     i+=1
     if i==100:
          break

# p.205
for i in range(10000):
     print(i)
     if i==100:
          break
     
# p.206
for i in range(100):
     if i%2==0:
          continue
     print(i) 

# p.207
i=0
while i<100:
     i+=1
     if i%2==0:
          continue
     print(i)

# p.208
count=int(input('반복할 횟수를 입력하세요: '))
i=0
while True:
     print(i)
     i+=1
     if i==count:
          break

# p.209
count=int(input('반복할 횟수를 입력하세요: '))   

for i in range(count+1):
     if i%2==0:
          continue
     print(i)

# 18.5 연습문제
i=0
while True:
     if i%10!=3:
          i=i+1
          continue
     if i>73:
          break
     print(i,end=' ')
     i+=1

# 18.6 심사문제
start, stop=map(int,input().split())
i=start
 
while True:
     if i%10==3:
          i=i+1
          continue
     elif i>stop:
          break
     print(i, end=' ')
     i +=1     

# p.214
for i in range(5):
     for j in range(5):
          print('j:',j,sep='',end=' ')
     print('i:', i, '\\n', sep='') 

for i in range(5):
     for j in range(5):
          print('*', end='')
     print()   

# p.215
for i in range(3):
     for j in range(7):
          print('*', end='')
     print()           

# p.216
for i in range(5):
     for j in range(5):
          if j<=i:
               print('*', end='')
     print()     

for i in range(5):
     for j in range(5):
          if j==i:
               print('*', end='')
     print()            
 
# p.217
for i in range(5):
     for j in range(5):
          if j==i:
               print('*', end='')
          else:
               print('',end='')     
     print()   

# 19.5 연습문제
for i in range(5):
     for j in range(5):
          if j<i:
               print('',end='')
          else:
               print('*',end='')
     print() 

# 19.6 심사문제
# 이거는 너무 어려워서 못했습니다. 죄송합니다....

# p.220
for i in range(1,101):
     print(i)

# p.221
for i in range(1,101):
     if i%3==0:
          print('Fizz')
     elif i%5==0:
          print('Buzz')
     else:
          print(i)

for i in range(1,101):
     if i%3==0 and i%5==0:
          print('FizzBuzz')
     elif i%3==0:
          print('Fizz') 
     elif i%5==0:
          print('Buzz')
     else:
          print(i)

# p.222
for i in range(1,101):
     if i%15==0:
          print('FizzBuzz')
     elif i%3==0:
          print('Fizz')
     elif(i%5==0):
          print('Buzz')
     else:
          print(i)

# p.223
for i in range(1,101):
     print('Fizz'* (i%3==0) + 'Buzz' * (i%5==0) or i)

# 20.7 연습문제
for i in range(1,101):
     if i%2==0 and i%11==0:
          print('FizzBuzz')
     elif i%2==0:
          print('Fizz')
     elif i%11==0:
          print('Buzz')
     else:
          print(i)

# 20.8 심사문제
num1, num2 = map(int, input().split())


for i in range(num1, num2+1):
    if i%5 == 0 and i%7 == 0:
        print("FizzBuzz")
    elif i%5 == 0:
        print('Fizz')
    elif i%7 == 0:
        print('Buzz')
    else:
        print(i)
print()    
                 