import csv
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# CSV 파일 읽기
with open('subwaytime.csv',	encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)

# 하차 인원 계산
data['하차인원'] = data.iloc[:, 11].astype(int) + data.iloc[:, 13].astype(int)

# 호선별 최대 하차 인원 및 역 이름 계산
max_station = data.groupby('호선명').apply(lambda x: x.loc[x['하차인원'].idxmax()])

# 결과 출력
for _, row in max_station.iterrows():
    print(f"출근 시간대 {row['호선명']} 최대 하차역 : {row['지하철역']}역, 하차인원: {row['하차인원']}명")

# 시각화
plt.figure(figsize=(12, 8))
plt.title('출근시간대 지하철 노선별 최대 하차 인원 및 하차역')

# 바 차트 데이터 준비
stations = max_station['호선명'] + ' ' + max_station['지하철역']
passengers = max_station['하차인원']

plt.bar(stations, passengers)
plt.xticks(rotation=90)
plt.xlabel('지하철역')
plt.ylabel('하차 인원')
plt.tight_layout()
plt.show()
