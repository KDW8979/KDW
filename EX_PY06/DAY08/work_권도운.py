# p. 303 연습문제
# path='C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'

# for a in path:
#     dot=path.find('.')
# print(path[dot+1 : ])

# p.305 24.5 심사문제
# msg=input()
# data=msg.split()
# count=0
# for m in data:
#     if 'the' in m:
#         if len(m)==3 or m[3]=="," or m[3]=='.':
#             count=count+1
#             print(m)
# print(count)

# 24.6 심사문제
price=list(map (int, input().split(';') ) )
price.sort(reverse=True)
for i in price:
    print('{0:>9,}'.format(i))

# 29.7 연습문제


