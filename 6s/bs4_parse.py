import requests
from bs4 import BeautifulSoup


res = requests.get('http://www.naver.com')
soup = BeautifulSoup(res.text, "html.parser")

print soup.prettify()