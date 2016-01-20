import os
from bs4 import BeautifulSoup
import requests

LAST_EP = 1630
BEGIN_EP = 1628

for i in range(LAST_EP, BEGIN_EP, -1):
    print "Getting Ep", i
    res = requests.get('http://www.xkcd.com/' + str(i))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')

    comic = soup.select('#comic')
    image = comic[0].select('img')

    getFile = requests.get('http:' + image[0]['src'])
    getFile.raise_for_status()

    downFile = open(os.path.join(os.getcwd(), str(i) + '.png'), 'wb')
    for chunk in getFile.iter_content(100000):
        downFile.write(chunk)
    downFile.close()
    print "Ep", i, "Done"