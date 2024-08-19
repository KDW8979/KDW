import requests
from bs4 import BeautifulSoup
from collections import Counter
from konlpy.tag import Okt
import collections
from PIL import	Image
import numpy as np
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import platform
if not hasattr(collections, 'Callable'):
    collections.Callable = collections.abc.Callable

urls = []
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
job_titles = []

for page_number in range(1, 5):
    url = f"https://www.saramin.co.kr/zf_user/search/recruit?searchType=search&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&keydownAccess=&searchword=%EA%B2%8C%EC%9E%84%20%ED%94%84%EB%A1%A0%ED%8A%B8%EC%97%94%EB%93%9C&panel_type=&search_optional_item=y&search_done=y&panel_count=y&preview=y&recruitPage={page_number}&recruitSort=relation&recruitPageCount=40&inner_com_type=&show_applied=&quick_apply=&except_read=&ai_head_hunting="
    response = requests.get(url, headers=headers)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    job_posts = soup.find_all('div', class_='item_recruit')

    for post in job_posts:
        title = post.find('div', class_='job_sector').text.strip()
        job_titles.append(title)  

okt = Okt()
stopwords = ['개발자', '모집', '채용','개발','게임','프론트엔드','수정일','외','등록', '정일', '일','웹', '백엔드','게임개발']
nouns = []
for title in job_titles:
    english_words = re.findall(r'\b[a-zA-Z]+\b', title)
    nouns.extend([word for word in english_words if word.lower() not in stopwords])
    korean_nouns = okt.nouns(title)
    nouns.extend([noun for noun in korean_nouns if noun not in stopwords])

korean_nouns = []
for title in job_titles:
    for noun in okt.nouns(title):
        if noun not in stopwords:
            korean_nouns.append(noun)

english_words = []
for title in job_titles:
    words = re.findall(r'\b[a-zA-Z]+\b', title)
    for word in words:
        if word.lower() not in stopwords:
            english_words.append(word)         

nouns = korean_nouns + english_words
word_count = Counter(nouns)
print(word_count.most_common(10))


if	platform.system()	==	'Windows':
	path =	r'c:\Windows\Fonts\malgun.ttf'
elif platform.system()	==	'Darwin':
	path = r'/System/Library/Fonts/AppleGothic'
else:
	path = r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'

img_mask =	np.array(Image.open('cloud.png'))
wordcloud = WordCloud(font_path=path, background_color='white',repeat=True,
colormap='spring',	mask=img_mask, width=800, height=600).generate_from_frequencies(word_count)

plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
