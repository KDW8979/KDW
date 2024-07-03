#----------------------------------------------
# [실습] 숫자 데이터를 10번 입력을 받습니다.
#        - 숫자 데이터를 모두 더해서 합계가 30이상이 되면
#          10번 입력 안 받았더라도 종료해주세요. 
#----------------------------------------------
# datas=list(int(input()))
# total=0
# for data in datas:
#     if total>=30:
#         break
#     total=total+data
#     if len(list(datas))==10:
#         break
# print(total)    
total=0

for cnt in range(10):
    data=int(input("숫자 입력 : "))
    total=total+data
    if total>=30: break