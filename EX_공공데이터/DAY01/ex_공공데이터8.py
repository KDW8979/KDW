import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

def draw_lowhigh_graph(start_year, month, day):
    f=open('daegu-utf-8.csv', encoding='utf-8-sig')
    data=csv.reader(f)
    next(data)
    high_temp=[]
    low_temp=[]
    x_year=[]

    for row in data:
        if row[-1] != '':
            date_string=row[0].split('-')   # 날짜 데이터를 미리 분리함
            if int(date_string[0])>=start_year:   # 문자열 값을 int형으로 변환해서 비교
                if int(date_string[1])==month and int(date_string[2])==day:
                    high_temp.append(float(row[-1]))
                    low_temp.append(float(row[-2]))
                    x_year.append(date_string[0])    # 연도 저장

    f.close()

    plt.figure(figsize=(20,4))
    plt.plot(x_year, high_temp, 'hotpink', marker='o', label='최고기온')    # 최고기온 그래프
    plt.plot(x_year, low_temp, 'royalblue', marker='s', label='최저기온')    # 최고기온 그래프

    plt.rcParams['axes.unicode_minus']=False    # 음수가 깨지는 것 방지'

    plt.legend(loc=2)
    plt.xlabel('year')
    plt.ylabel('temperature')
    plt.show()

draw_lowhigh_graph(2020,12,17)    