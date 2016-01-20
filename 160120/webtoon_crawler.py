import os
import requests
from bs4 import BeautifulSoup


WEBTOON_NAME = 'hanobaek'

print "Trying to requeset..."
res = requests.get('http://comics.nate.com/webtoon/detail.php?btno=48746&bsno=277282&category=1')
res.raise_for_status()
print "Got response"

soup = BeautifulSoup(res.text, "html.parser")
result = soup.select('.toonView')
image = result[0].select('img')

newDirPath = os.path.join(os.getcwd(), WEBTOON_NAME)
os.mkdir(newDirPath)

for i in range(0, len(image)):
    print "Downloading image", i
    cut = requests.get(image[i]['src'])
    cutFile = open(os.path.join(newDirPath, str(i) + '.jpg'), 'wb')

    for chunk in cut.iter_content(100000):
        cutFile.write(chunk)

    cutFile.close()

print "Done"
