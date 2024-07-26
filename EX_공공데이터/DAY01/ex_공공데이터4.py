import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

f=open('daegu-utf-8.csv', encoding='utf-8-sig')
data=csv.reader(f)

header=next(data)
result=[]

for row in data:
    if row[4] !='':     # 최고 기온 데이터 값이 있으면, 리스트에 저장
        result.append(float(row[4]))

print(len(result))
f.close()
plt.figure(figsize=(10,2))
plt.plot(result,'r')    # result 리스트에 저장된 값을 빨간색 그래프로 그리기
plt.show()        