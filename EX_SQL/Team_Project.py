import pymysql
import pandas as pd
import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

conn = pymysql.connect(host='172.20.131.64', user='dowoon', password='1234', db='minipj', charset='utf8')
cur = conn.cursor()
query = """
SELECT u.*, c.*
FROM unemployer u
inner join consumer as c on u.year = c.year
"""
cur.execute(query)
rows = cur.fetchall()
columns = [desc[0] for desc in cur.description]
df = pd.DataFrame(rows, columns=columns)
cur.close()
conn.close()


years = df['Year']
unemployment_rate = df['Unemployment Rate']
rise=df['rise']
plt.figure(figsize=(10, 10))
plt.plot(years, unemployment_rate, marker='o', label='Unemployment Rate')
plt.plot(years, rise, marker='o', label='rise')
plt.title('실업률과 물가상승률의 관계', fontsize=20)
plt.xlabel('Year')
plt.ylabel('Rate (%)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

years = df['Year']
unemployment_rate = df['Youth Unemployment Rate']
rise=df['rise']
plt.figure(figsize=(10, 10))
plt.plot(years, unemployment_rate, marker='o', label='Youth Unemployment Rate')
plt.plot(years, rise, marker='o', label='rise')
plt.title('청년실업률과 물가상승률의 관계', fontsize=20)
plt.xlabel('Year')
plt.ylabel('Rate (%)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

years = df['Year']
unemployment_rate = df['Senior Unemplyment Rate']
rise=df['rise']
plt.figure(figsize=(10, 10))
plt.plot(years, unemployment_rate, marker='o', label='Senior Unemplyment Rate')
plt.plot(years, rise, marker='o', label='rise')
plt.title('노인실업률과 물가상승률의 관계', fontsize=20)
plt.xlabel('Year')
plt.ylabel('Rate (%)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()