# p.244
a=[10,20,30]
a.append(500)
print(a, len(a))

# p.245
a=[]
a.append(10)
print(a)

a=[10,20,30]
a.append([500,600])
print(a, len(a))

# p.246
a=[10,20,30]
a.extend([500,600])
print(a, len(a))

a=[10,20,30]
a.insert(2,500)
print(a, len(a))

a=[10,20,30]
a.insert(0,500)
print(a)

a=[10,20,30]
a.insert(len(a),500)
print(a)

# p.248
a=[10,20,30]
a.insert(1, [500,600])
print(a)

a=[10,20,30]
a[1:1] = [500,600]
print(a)

a=[10,20,30]
a.pop()
print(a)

# p.249
a=[10,20,30]
a.pop(1)
print(a)

a=[10,20,30]
del a[1]
print(a)

a=[10,20,30,20]
a.remove(20)
print(a)

# p.250
a=[10, 20, 30, 15, 20, 40]
print(a.index(20))

a=[10, 20, 30, 15, 20, 40]
print(a.count(20))

# p.252
a=[10, 20, 30, 15, 20, 40]
a.reverse()
print(a)

a=[10, 20, 30, 15, 20, 40]
a.sort()   # a의 내용을 변경하여 정렬
print(a)

b=[10, 20, 30, 15, 20, 40]
print(sorted(b))  # 정렬된 새 리스트를 작성

a=[10,20,30]
a.clear()
print(a)

# p.253
a=[10,20,30]
del a[:]
print(a)

a=[10,20,30]
a[len(a):]=[500]
print(a)

a=[10,20,30]
a[len(a):]=[500,600]
print(a)

# p.254
# if not len(seq):  # 리스트가 비어 있으면 True
# if len(seq):      # 리스트에 요소가 있으면 True       

# if not seq:       # 리스트가 비어 있으면 True
# if seq:           # 리스트에 내용이 있으면 True

seq=[10,20,30]
print(seq[-1])

# a=[]
# print(a[-1])      # ERROR!!

seq=[]
if seq:             # 리스트에 요소가 있는지 확인
    print(seq[-1])  # 요소가 있을 때만 마지막 요소를 가져옴

a=[0,0,0,0,0]
b=a

# p.255
print(a is b)

b[2]=99
print(a)
print(b)

a=[0,0,0,0,0]
b=a.copy()

print(a is b)
print(a==b)

# p.256
b[2]=99
print(a)
print(b)

a=[38,21,53,62,19]
for i in a:
    print(i)

# p.257
for i in [38,21,53,62,19]:
    print(i)

a=[38,21,53,62,19]
for index, value in enumerate(a):
    print(index, value)

for index, value in enumerate(a):
    print(index+1, value)

# p.258
for index, value in enumerate(a, start=1):
    print(index, value)

a=[38,21,53,62,19]
for i in range(len(a)):
    print(a[i])

a=[38,21,53,62,19]
i=0
while i<len(a):
    print(a[i])
    i+=1

# p.259
a=[38,21,53,62,19]
i=0
# while i<=len(a):
#     print(a[i])
#     i+=1
while i<len(a):
    print(a[i])
    i+=1

a=[38,21,53,62,19]
smallest=a[0]
for i in a:
    if i<smallest:
        smallest=i
print(smallest)        

# p.260
a=[38,21,53,62,19]
largest=a[0]
for i in a:
    if i>largest:
        largest=i
print(largest)        

a=[38,21,53,62,19]
a.sort()
print(a[0])
a.sort(reverse=True)
print(a[0])

a=[38,21,53,62,19]
print(min(a))
print(max(a))

# p.261

a=[10,10,10,10,10]
x=0
for i in a:
    x+=i
print(x)  

a=[10,10,10,10,10]
print(sum(a))

# p.262
a=[i for i in range(10)]       # 0부터 9까지 숫자를 생성하여 리스트 생성
print(a)
b=list(i for i in range(10))   # 0부터 9까지 숫자를 생성하여 리스트 생성
print(b)

c=[i+5 for i in range(10)]
print(c)
d=[i*2 for i in range(10)]
print(d)

# p.263
a=[i for i in range(10) if i%2==0]     # 0~9 숫자 중 2의 배수인 숫자(짝수)로
print(a)                               # 리스트 생성

b=[i+5 for i in range(10) if i%2==1]   # 0~9 숫자 중 홀수에 5를 더하여
print(b)                               # 리스트 생성

a=[i*j for j in range(2,10) for i in range(1,10)]

# p.264
a=[i*j for j in range(2,10)
       for i in range(1,10)]

a=[1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
    a[i]=int(a[i])
print(a)    

# p.265
a=[1.2, 2.5, 3.7, 4.6]
a=list(map(int,a))
print(a)

a= list(map(str,range(10)))
print(a)

# a=input().split()
# print(a)

# p.266

# a=map(int,input().split())
# print(a, list(a))

a,b=[10,20]
print(a)
print(b)

# x=input().split()  # input().split()의 결과는 문자열 리스트
# m=map(int,x)       # 리스트의 요소를 int로 변환, 결과는 맵 객체
# a,b=m              # 맵 객체는 변수 여러 개에 저장할 수 있음

# p.267
a=(38,21,53,62,19,53)
print(a.index(53))

a=(10,20,30,15,20,40)
print(a.count(20))

a= (38,21,53,62,19,53)
for i in a:
    print(i, end=' ')

# p.268
a=tuple(i for i in range(10) if i%2==0)
print(a)

a=(1.2,2.5,3.7,4.6)
a=tuple(map(int,a))
print(a)

a=(38,21,53,62,19)
print(min(a))
print(max(a))
print(sum(a))

# 22.9 연습문제
a=['alpha','bravo','charlie','delta','echo','foxtrot', 'golf', 'hotel', 'india']
b=[i for i in a if len(i)==5]
print(b)

# 22.10 심사문제
num1, num2 = map(int, input().split())
result = [2 ** i for i in range(num1, num2 + 1)]
if 1<=num1<=20 and 10<=num2<=30:    
    result.pop(1)
    result.pop(-2)
    print(result)
else:
    print() 


# p.313
x={'a':10, 'b':20, 'c':30, 'd':40}
x.setdefault('e')
print(x)

# p.314
x.setdefault('f',100)
print(x)

x={'a':10, 'b':20,'c':30,'d':40}
x.update(a=90)
print(x)

x.update(e=50)
print(x)

x.update(a=900,f=60)
print(x)

y={1:'one',2:'two'}
y.update({1:'ONE',3:'THREE'})
print(y)

# p.315
y.update([[2,'TWO'],[4,'FOUR']])
print(y)  

y.update(zip([1,2],['one','two']))
print(y)

x={'a':10, 'b':20,'c':30,'d':40}
x.setdefault('a',90)
print(x)

x={'a':10, 'b':20,'c':30,'d':40}
x.pop('a')
print(x)

# p.316
x={'a':10, 'b':20,'c':30,'d':40}
del x['a']
print(x)

x={'a':10, 'b':20,'c':30,'d':40}
x.popitem()
print(x)

# p.317
x={'a':10, 'b':20,'c':30,'d':40}
x.clear()
print(x)

x={'a':10, 'b':20,'c':30,'d':40}
x.get('a')
print(x)

x.get('z',0)
print(x)

x={'a':10, 'b':20,'c':30,'d':40}
x.items()
print(x)

print(x.keys())

# p.318
print(x.values())

keys=['a','b','c','d']
x=dict.fromkeys(keys)
print(x)

y= dict.fromkeys(keys,100)
print(y)

# p.319
x={'a':10, 'b':20,'c':30,'d':40}
for i in x:
    print(i, end=' ')

# p.320
x={'a':10, 'b':20,'c':30,'d':40}
for key, value in x.items():
    print(key, value)

x={'a':10, 'b':20,'c':30,'d':40}
for key in x.keys():
    print(key, end=' ')

x={'a':10, 'b':20,'c':30,'d':40}
for value in x.values():
    print(value, end=' ')        

    