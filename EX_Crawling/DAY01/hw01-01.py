from bs4 import BeautifulSoup
from urllib.request import urlopen


def scraping_use_find(html):
    div_class=html.find_all('div class="tombstone-container"')






   

def main():
    page = urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168')
    html=BeautifulSoup(page.read(), 'html.parser')

    print('National Weather Service Scraping')
    print('----------------------------------')

    scraping_use_find(html)
    # scraping_use_select(html)

main()

