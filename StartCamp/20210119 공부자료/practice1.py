import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex'
response = requests.get(url).text

soup = BeautifulSoup(response, 'html.parser')

text = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text

print(f'현재 원/달러 환율은 {text}입니다.')