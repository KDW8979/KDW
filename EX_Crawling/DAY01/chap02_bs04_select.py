from bs4 import BeautifulSoup
soup=BeautifulSoup(html_example, 'html.parser')
head=soup.select_one('head')
print(head)
print('head.text: ', head.text.strip())