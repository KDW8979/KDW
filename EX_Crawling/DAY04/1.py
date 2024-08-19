import requests
from bs4 import BeautifulSoup
from collections import Counter
from konlpy.tag import Okt

import collections
if not hasattr(collections, 'Callable'):
    collections.Callable = collections.abc.Callable

urls = []
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
for page_number in range(1,5):
    urls.append(f"https://www.saramin.co.kr/zf_user/search/recruit?searchType=search&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&keydownAccess=&searchword=%EA%B2%8C%EC%9E%84+%EA%B0%9C%EB%B0%9C%EC%9E%90&panel_type=&search_optional_item=y&search_done=y&panel_count=y&preview=y&recruitPage={page_number}&recruitSort=relation&recruitPageCount=100&inner_com_type=&show_applied=&quick_apply=&except_read=&ai_head_hunting=&mainSearch=n")
    # print(urls)

    for url in urls:
        # url//2 = 'https://www.saramin.co.kr/zf_user/search/recruit?searchType=search&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&keydownAccess=&searchword=%EA%B2%8C%EC%9E%84%20%EA%B0%9C%EB%B0%9C%EC%9E%90&panel_type=&search_optional_item=y&search_done=y&panel_count=y&preview=y&recruitPage=2&recruitSort=relation&recruitPageCount=100&inner_com_type=&show_applied=&quick_apply=&except_read=&ai_head_hunting=&mainSearch=y'

        response = requests.get(url, headers=headers)
        # print(response)
        html_content = response.text
        # print(html_content)
        # BeautifulSoup 객체 생성
        soup = BeautifulSoup(html_content, 'html.parser')
        print(soup)

        # 채용 공고 찾기 (클래스나 ID를 사용하여 더 구체적으로 지정)
        job_posts = soup.find_all('div', class_='item_recruit')

        # 각 채용 공고에서 정보 추출
        for post in job_posts:
            # 예: 제목 추출
            title = post.find('h2', class_='job_tit').text.strip()
            # 예: 회사명 추출
            company = post.find('strong', class_='corp_name').text.strip()
            
            print(f"Title: {title}")
            print(f"Company: {company}")
            print("---")

