import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib
import re

f= open('gender.csv', encoding='euc_kr')
data=csv.reader(f)

city_list=['대구광역시', '대구광역시 중구', '대구광역시 동구', '대구광역시 서구', '대구광역시 남구', '대구광역시 북구', '대구광역시 수성구',
      '대구광역시 달서구', '대구광역시 달성군', '대구광역시 군위군']
male_count=0
female_count=0

for row in data:
    for i in range(1,len(city_list)):
        if city_list[i] in row[0]:
            male_count=int(row[104].replace(',',''))
            female_count=int(row[207].replace(',',''))
            print(f'{city_list[i]}: (남: {male_count} 여: {female_count})')
            break

def draw_pie_chart():
    fig,ax=plt.subplot(5,2)
    for i in range(1,6):
        for j in range(2):
            ax[i,j].pie(data)
        
        

    
    



