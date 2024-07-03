#----------------------------------------------------------
# [실습1] 글자를 입력 받습니다
#         입력 받은 글자의 (a~z, A~Z) 코드값을 출력합니다.
#----------------------------------------------------------

data=input("글자 입력(a~z, A~Z): ")

# 문자==> 코드값 변환 내장함수 : ord(문자1개)
# if len(data)>0:
#     if len(data)==1:
#         if 'a'<=data<='z' or 'A'<=data<='Z'
#         print(f'{data}의 코드값 : {ord(data)}')
#         else: 
#         print('대문자, 소문자 알파벳만 가능합니다.')   
#     else:    
#         print('1개 문자만 입력해야 합니다.')
    
# else:
#     print('입력된 데이터가 없습니다.')

if len(data)==1 and ('a'<=data<='z' or 'A'<=data<='Z'):
    print(f'{data}의 코드값 : {ord(data)}')
else: 
    print('1개의 알파벳 문자만 입력해야 합니다.\n입력된 데이터를 확인하세요.')



data="Ab"
# ord(data[0])
# ord(data[1])
print(list(map(ord,data)))

#----------------------------------------------------------
# [실습2] 점수를 입력 받은 후 학점을 출력합니다.
# - 학점: A+, A, A-, B+, B, B-, C+, C, C-, D+, D, D-, F
# A+ : 96~100
# A : 95
# A- : 90~94        
#----------------------------------------------------------

# score=input("점수를 입력하십시오. : ")
# score=int(score)
# if score>=0 and score<=100:
#     if score >=96 and score<=100:
#         print('당신의 학점은 A+입니다.')
#     elif score==95:
#         print('당신의 학점은 A입니다.')
#     elif score>=90 and score<95:
#         print('당신의 학점은 A-입니다.')
#     elif score>=86 and score<90:
#         print('당신의 학점은 B+입니다.')    
#     elif score==85:
#         print('당신의 학점은 B입니다.')    
#     elif score>=80 and score<85:
#         print('당신의 학점은 B-입니다.')    
#     elif score>=76 and score<80:
#         print('당신의 학점은 C+입니다.') 
#     elif score==75:
#         print('당신의 학점은 C입니다.')    
#     elif score>=70 and score<75:
#         print('당신의 학점은 C-입니다.')    
#     elif score>=66 and score<70:
#         print('당신의 학점은 D+입니다.')     
#     elif score==65:
#         print('당신의 학점은 D입니다.')     
#     elif score>=60 and score<65:
#         print('당신의 학점은 D-입니다.')     
#     else:
#         print('당신의 학점은 F입니다.')
# else:
#     print('잘못된 점수를 입력했습니다.')            


    