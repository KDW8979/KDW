import csv

def get_index_of_age_csv():
    f=open('age.csv', encoding='euc_kr')
    data=csv.reader(f)
    header=next(data)

    print('------------------------------------------------------')
    print('age.csv index')
    print('------------------------------------------------------')
    for i in range(len(header)):
        print(f'[{i:3}]: {header[i]}')      # {1:4}: 4자리 공간에 i값 출력

    f.close()

print(get_index_of_age_csv())