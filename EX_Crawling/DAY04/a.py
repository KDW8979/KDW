import requests
from bs4 import BeautifulSoup
from collections import Counter
from konlpy.tag import Okt
import collections
from PIL import Image
import numpy as np
import platform
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Callable 오류 수정 (Python 3.10 이상)
if not hasattr(collections, 'Callable'):
    collections.Callable = collections.abc.Callable

# URL 및 헤더 설정
urls = []
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
job_sectors = []

# 1단계: 채용 공고 스크래핑
for page_number in range(1, 5):
    url = f"https://www.saramin.co.kr/zf_user/search/recruit?searchType=search&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&keydownAccess=&searchword=%EA%B2%8C%EC%9E%84+%ED%94%84%EB%A1%A0%ED%8A%B8%EC%97%94%EB%93%9C&panel_type=&search_optional_item=y&search_done=y&panel_count=y&preview=y&recruitPage={page_number}&recruitSort=relation&recruitPageCount=100&inner_com_type=&show_applied=&quick_apply=&except_read=&ai_head_hunting=&mainSearch=n"
    response = requests.get(url, headers=headers)
    html_content = response.text

    # BeautifulSoup 객체 생성
    soup = BeautifulSoup(html_content, 'html.parser')

    # job_sector 텍스트 추출
    sectors = soup.find_all('div', class_='job_sector')
    for sector in sectors:
        job_sectors.append(sector.text.strip())

# 2단계: 키워드 추출 및 불용어 제거
okt = Okt()
nouns = []
stopwords = ['개발자', '모집', '채용', '개발', '게임', '경력무관']  # 불용어 리스트

for sector in job_sectors:
    for noun in okt.nouns(sector):
        if noun not in stopwords:
            nouns.append(noun)

word_count = Counter(nouns)

# 3단계: Word Cloud 생성 및 출력
if platform.system() == 'Windows':
    path = r'c:\Windows\Fonts\malgun.ttf'
elif platform.system() == 'Darwin':
    path = r'/System/Library/Fonts/AppleGothic'
else:
    path = r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'

# 이미지 마스크 설정 (gamepad.png 이미지 필요)
img_mask = np.array(Image.open('gamepad.png'))

wordcloud = WordCloud(font_path=path, background_color='white', repeat=True,
                      colormap='viridis', mask=img_mask, width=800, height=600).generate_from_frequencies(word_count)

plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()





