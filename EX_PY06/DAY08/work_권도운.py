# # 24.4 연습문제
path='C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'

for a in path:
    dot=path.find('.')
print(path[dot+1 : ])

# # 24.5 심사문제
msg=input().split()
count=0
for words in msg:
    if words.strip('",.')=='the':
        count=count+1
print(count)        


# # 24.6 심사문제
a=list(map(int,input().split(';')))
a.sort(reverse=True)
for price in a:
    print('{:>9,}'.format(price))

# # 29.7 연습문제
x=10
y=3
def get_quotient_remainder(a,b):
    return a//b, a%b

quotient, remainder = get_quotient_remainder(x,y)
print('몫: {0}, 나머지: {1}'.format(quotient, remainder))

# # 29.8 심사문제
x,y=map(int, input().split())

def calc(a,b):
    return a+b, a-b, a*b, a/b
a,s,m,d=calc(x,y)
print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a,s,m,d))

# # 30.6 연습문제
korean, english, mathematcs, science= 100, 86, 81, 91
def get_max_score(*args):
    return(max(args))

max_score=get_max_score(korean, english, mathematcs, science)
print('높은 점수 :', max_score)

max_score= get_max_score(english, science)
print('높은 점수:', max_score)

# 30.7 심사문제

korean, english, mathematcs, science= map(int, input().split())
def get_min_max_score(*args):
    return min(args), max(args) 
def get_average(**kwargs):
    return (sum(kwargs.values())/len(kwargs))

min_score, max_score = get_min_max_score(korean, english, mathematcs, science)
average_score=get_average(korean=korean, english=english, mathematcs=mathematcs, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score, max_score, average_score))

min_score, max_score=get_min_max_score(english, science)
average_score=get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score, max_score, average_score))
