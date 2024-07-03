# p. 186
for i in range(100):
    print('Helo world!')
# p.187
for i in range(100):
    print('Hello, world!', i)

# p.188
for i in range(5,12):
    print('Hello, world!',i)

for i in range(0,10,2):
    print('Hello, world!',i)   

# p.189
# for i in range(10,0):           <== range(10,0)은 동작하지 않음
#     print('Hello, world!',i)

for i in range(10,0,-1):
        print('Hello, world!',i)

for i in reversed(range(10)):
    print('Hello, world!',i)

# p.190
count = int(input('반복할 횟수를 입력하세요: '))

for i in range(count):
    print('Hello, world!', i)

# p.191
a=[10,20,30,40,50]
for i in a:
     print(i)

fruits=('apple','orange', 'grape')
for f in fruits:
     print(f)

for letter in 'Python':
     print(letter, end=' ')     

# p.192
for letter in reversed('Python'):
     print(letter, end=' ')


# 16.5 연습문제
x=[49,-17,25,102,8,62,21]
for i in x:
     print(i*10, end=' ')         

# 16.6 심사문제
x=int(input())
y=range(1,10)
if 2<=int(x)<=9:
     for b in y:
          print(f'{x} * {b} = {x*b}')   
else:
     print('숫자는 2~9까지만 입력 가능합니다.')          
            