#----------------------------------------------------------
# Dict 자료형 살펴보기
# - 연산자와 내장함수
#----------------------------------------------------------
person={'name':'홍길동', 'age':20, 'job':'학생'}
dog={'race':'허스키', 'weight':'80kg', 'color':'검정', 'gender':'남', 'age':10}
jumsu={'국어':90, '수학':178, '체육':100}
## [연산자]----------------------------------------------------------------------
# 산술 연산 X
# person+dog

# 멤버 연산자
#      key
print('name' in dog)
print('name' in person)

#      value : dict 타입에서는 key만 멤버 연산자로 확인
print('허스키' in dog)
print(20 in person)

# value 추출
print('허스키' in dog.values())
print(20 in person.values())

## [내장함수]---------------------------------------------------------------------
## - 원소/요소 개수 확인 :len()
print(f'dog의 요소 개수 : {len(dog)}')
print(f'person의 요소 개수 : {len(person)}')

## - 원소/요소 정렬 : sorted()
# - 키만 정렬
print(f'person 오름차순정렬 : {sorted(person)}')
print(f'person 내림차순 정렬 : {sorted(person,reverse=True)}')
print(f'jumsu 값 오름차순 정렬: {sorted(jumsu.values())}')
print(f'jumsu 키 오름차순 정렬: {sorted(jumsu)}')
# jumsu 값 오름차순 정렬: [90, 100, 178]
# jumsu 키 오름차순 정렬: ['국어', '수학', '체육']
print(f'jumsu값 오름차순 정렬: {sorted(jumsu.items())}')
#jumsu값 오름차순 정렬: [('국어', 90), ('수학', 178), ('체육', 100)]
print(f'jumsu값 오름차순 정렬 : {sorted(jumsu.items(), key=lambda x:x[1])}')

## - 동일한 타입에서 정렬 가능함

