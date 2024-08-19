from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import Request

melon_url = 'https://www.melon.com/chart/index.htm'

urlrequest=Request(melon_url, headers={'User-Agent': 'Mozilla/5.0'})

html = urlopen(urlrequest)

soup= BeautifulSoup(html.read(), 'html.parser')
print(soup)