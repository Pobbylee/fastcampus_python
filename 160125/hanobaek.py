# coding=euc-kr

import os
import requests
from bs4 import BeautifulSoup

# 다운로드 할 첫 화와 끝 화를 설정해줍니다
BEGIN_EPISODE = 1
LAST_EPISODE = 10
WEBTOON_NAME = 'hanobaek'

# 다운 받은 파일들이 저장될 디렉토리를 생성해줍니다
# 이 때, 같은 이름의 디렉토리가 이미 있다면 에러가 뜹니다
newDirPath = os.path.join(os.getcwd(), WEBTOON_NAME)
os.mkdir(newDirPath)

# 일단 첫 화 링크로 접근합니다
print "Trying to request to get EPISODE URLs..."
res = requests.get('http://comics.nate.com/webtoon/detail.php?btno=48746&bsno=277282&category=1')
res.raise_for_status()
print "Got response"

# 상단 오른쪽의 에피소드를 선택할 수 있는 목록을 파싱하여 매 화마다의 주소들을 리스트로 얻어옵니다
soup = BeautifulSoup(res.text, "html.parser")
result = soup.select('#tnt_customSelect > ul > li > a')

print "Got URLs. Start to download images"

# 매 화마다 해당 링크로 리퀘스트를 날리고 각 에피소드의 이미지들을 다운로드 하는 반복문입니다
for ep in range(-BEGIN_EPISODE, -LAST_EPISODE - 1, -1):
    print "----------------------------------------"
    print "Trying to request EP", str(-ep) + "'s images..."

    # 해당 에피소드 링크에 리퀘스트를 날립니다
    epResponse = requests.get('http://comics.nate.com' + result[ep]['href'])
    epResponse.raise_for_status()
    print "Got response"

    # 해당 에피소드가 있는 페이지의 이미지들을 파싱합니다
    imageParser = BeautifulSoup(epResponse.text, "html.parser")
    images = imageParser.select('.toonView > img')

    # 에피소드 내의 이미지만 담을 에피소드 디렉토리를 새로 생성해줍니다
    # 이 때도 마찬가지로 이미 디렉토리가 있다면 에러가 뜹니다
    epDirPath = os.path.join(newDirPath, 'EP ' + str(-ep))
    os.mkdir(epDirPath)

    # 해당 에피소드의 이미지 리스트들을 반복하여 다운로드합니다
    for i in range(0, len(images)):
        print "Downloading images", str(-ep) + "-" + str(i)
        cut = requests.get(images[i]['src'])

        # 저장될 이미지 파일을 생성합니다 (ex. '2-1.jpg', '5-2.jpg')
        cutFile = open(os.path.join(epDirPath, str(-ep) + "-" + str(i) + '.jpg'), 'wb')

        for chunk in cut.iter_content(100000):
            cutFile.write(chunk)

        cutFile.close()

print "\nDone"
