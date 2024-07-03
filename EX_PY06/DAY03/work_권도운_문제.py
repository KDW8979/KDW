# 1번
print("Hello World")

# 2번
print("Mary's cosmetics")

# 3번
print('신씨가 소리질렀다. "도둑이야."')

# 4번
print("c:\\Windows")

# 5번
print('안녕하세요.\n만나서\t\t반갑습니다.') # ==> \n : 줄바꾸기, \t : 탭

# 6번
print("오늘은", "일요일") # ==> 오늘은 일요일   ,가 있으면 한 칸 띄워서 출력됨

# 7번
print("naver", "kakao", "sk", "samsung", sep=";")

# 8번
print("naver", "kakao", "sk", "samsung", sep="/")

# 9번
print("first",end=''); print("second")

# 10번
print(5/3)

# 11번
삼성전자=50000
총평가금액= 삼성전자*10
print(총평가금액)

# 12번
시가총액=298000000000000
현재가=50000
PER=15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))

# 13번
s="hello"
t="python"
print(s+'!', t)

# 14번
print(2+2*3)

# 15번
a="132"
print(type(a))

# 16번
num_str="720"
num_int=int(num_str)
print(num_int,type(num_int))

# 17번
num=100
num_str=str(num)
print(num_str, type(num_str))

# 18번
data="15.79"
data=float(data)
print(data, type(data))

# 19번
year="2020"
print((int(year))-1)
print((int(year))-2)
print((int(year))-3)

# 20번
fee=48584
month=36
print(fee*month)

# 21번
letters='python'
print(letters[0],letters[2])

# 22번
license_plate="24가 2210"
print(license_plate[-4:])

# 23번
string="홀짝홀짝홀짝"
print(string[::2])

# 24번
string="PYTHON"
print(string[::-1])

# 27번
url="http://sharebook.kr"
print(url[-2:])

# 28번
lang='python'
lang[0]='P'
print(lang) # ==> 문자열은 수정할 수가 없다. 그래서 오류가 난다

# 31번
a="3"
b="4"
print(a+b) # ==> "34"

# 32번
print("Hi"*3) # ==> HiHiHi

# 33번
print("-"*80)

# 34번
t1='python'
t2='java'
print((t1 + ' ' + t2 + ' ' )*3)

# 35번
name1="김민수"
age1=10
name2="이철희"
age2=13

print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))

# 37번
name1="김민수"
age1=10
name2="이철희"
age2=13

print(f'이름: {name1} 나이: {age1}')
print(f'이름: {name2} 나이: {age2}')

# 39번
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

# 51번
movie_rank=["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)

#54번
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del movie_rank[3]
print(movie_rank)

# 55번
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[2]
del movie_rank[2]
print(movie_rank)

# 56번
lang1=["C","C++","JAVA"]
lang2=["Python","Go","C#"]
langs=lang1+lang2
print(langs) 

# 57번
nums=[1,2,3,4,5,6,7]
print(f'max: {max(nums)}')
print(f'min: {min(nums)}')

# 58번
nums=[1,2,3,4,5]
print(sum(nums))

# 59번
cook=["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 60번
nums=[1,2,3,4,5]
average=sum(nums)/len(nums)
print(average)

# 61번
price=['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 62번
nums=[1,2,3,4,5,6,7,8,9,10]
print(nums[0::2])

# 63번
nums=[1,2,3,4,5,6,7,8,9,10]
print(nums[1::2])

# 64번
nums=[1,2,3,4,5]
print(nums[::-1])

# 65번
interest=['삼성전자', 'LG전자', 'Naver']
print('출력 예시:\n' + interest[0] , interest[2])

# 70번
data=[2,4,3,1,5,10,9]
print(sorted(data))

# 71번
my_variable=()
print(my_variable, type(my_variable))

# 72번
movie_rank=('닥터 스트레인지', '스플릿', '럭키')
print(movie_rank, type(movie_rank))

# 73번
num=(1,)
print(num, type(num))

# 74번
# t=(1,2,3)
# t[0]='a'
# Traceback (most recent call last):
#   File "c:\Users\kdp\Desktop\EX_PY06\DAY03\work_권도운_71~80.py", line 15, in <module>
#     t[0]='a'
# TypeError: 'tuple' object does not support item assignment  ===> tuple은 요소값을 변경할 수 없기 때문에 오류가 났다.

# 75번
t=1,2,3,4  # ==> tuple

# 76번
t=('a','b','c')
data=list(t)
data[0]='A'
t=tuple(data)
print(t, type(t))

# 77번
interest=('삼성전자', 'LG전자', 'SK Hynix')
data=list(interest)
print(data, type(data))

# 78번
interest=['삼성전자', 'LG전자', 'SK Hynix']
data=tuple(interest)
print(data, type(data))

# 79번
temp=('apple', 'banana', 'cake')
a,b,c= temp
print(a,b,c)

# 80번
(2,4,6,8,...,98)
nums=tuple(range(2,100,2))
print(nums)