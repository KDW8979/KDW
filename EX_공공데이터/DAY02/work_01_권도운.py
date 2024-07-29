import	csv
import	matplotlib.pyplot as	plt
import	platform
import	koreanize_matplotlib

with open('subwaytime.csv',	encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)
   

    max_passenger=[0]*7
    max_station=[0]*7

    for row in data:
        for i in range(1,8):
            if (row[1]==f'{i}호선') & (max_passenger[i-1]<int(row[11])+int(row[13])):
                a= int(row[11])+int(row[13])
                max_passenger[i-1]=a
                max_station[i-1]=f'{i}호선 {row[3]}'


    for i in range(1,8):
        print(f'출근 시간대 {i}호선 최대 하차역 : {max_station[i-1]}역, 하차인원: {max_passenger[i-1]}명')
 
plt.figure(figsize=(10,	10))
plt.title('출근시간대 지하철 노선별 최대 하차 인원 및 하차역')
plt.bar(max_station, max_passenger)
plt.xticks(range(7), labels=max_station, rotation=80)
plt.tight_layout()
plt.show()