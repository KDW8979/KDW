import pymysql
import pandas as pd

# MySQL 연결 설정
connection = pymysql.connect(
    host= '172.20.60.151',      # MySQL 서버 주소
    user='dowoon',  
    password='1234',  
    db='web_project',    
    # charset='utf8',     
    # cursorclass=pymysql.cursors.DictCursor
)

try:
   
    query = "SELECT id,category,text FROM health"  
    df = pd.read_sql(query, connection)

    # 결과 출력 (DataFrame)
    print(df)

finally:
    # 연결 종료
    connection.close()