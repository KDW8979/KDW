from konlpy.tag import Okt
okt= Okt()

list1= okt.pos("아버지 가방에 들어가신다.", norm=True, stem=True)
list2= okt.pos("아버지 가방에 들어가신다.", norm=False, stem=False)
print(list1)
print(list2)

word1= okt.pos("그래요ㅋㅋ?", norm=True, stem=True)
word2= okt.pos("그래욬ㅋㅋ?", norm=False, stem=True)
word3= okt.pos("그래욬ㅋ?", norm=True, stem=False)
print(word1)
print(word2)
print(word3)