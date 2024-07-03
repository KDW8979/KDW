# [1] 구구단 전체 출력 => 중첩 For ==> For 1개로
for i in range(20, 100):
    if i % 10 == 0:
        print(f'{int(i / 10)}단')
    else:
        print(f'{i // 10} * {i % 10} = {(i // 10) * (i % 10)}')


     



# [2] 구구단 전체 출력 => 가로로 출력 : 중첩 For, For 1개 
for j in range(1,10):
    for i in range(2,10):
            print(f'{i} * {j} = {i*j}',end='\t')
        
    print()


             

