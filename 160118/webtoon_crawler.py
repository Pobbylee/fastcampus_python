import requests
from bs4 import BeautifulSoup


res = requests.get('http://comic.naver.com/webtoon/detail.nhn?titleId=602921&no=1&weekday=thu')
soup = BeautifulSoup(res.text, "html.parser")
result = soup.find_all('div', attrs={'class': 'wt_viewer'})

image = result[0].find_all('img')

for i in range(0, len(image)):
    print image[i]['src']
