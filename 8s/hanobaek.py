# coding=euc-kr

import os
import requests
from bs4 import BeautifulSoup

# �ٿ�ε� �� ù ȭ�� �� ȭ�� �������ݴϴ�
BEGIN_EPISODE = 1
LAST_EPISODE = 10
WEBTOON_NAME = 'hanobaek'

# �ٿ� ���� ���ϵ��� ����� ���丮�� �������ݴϴ�
# �� ��, ���� �̸��� ���丮�� �̹� �ִٸ� ������ ��ϴ�
newDirPath = os.path.join(os.getcwd(), WEBTOON_NAME)
os.mkdir(newDirPath)

# �ϴ� ù ȭ ��ũ�� �����մϴ�
print "Trying to request to get EPISODE URLs..."
res = requests.get('http://comics.nate.com/webtoon/detail.php?btno=48746&bsno=277282&category=1')
res.raise_for_status()
print "Got response"

# ��� �������� ���Ǽҵ带 ������ �� �ִ� ����� �Ľ��Ͽ� �� ȭ������ �ּҵ��� ����Ʈ�� ���ɴϴ�
soup = BeautifulSoup(res.text, "html.parser")
result = soup.select('#tnt_customSelect > ul > li > a')

print "Got URLs. Start to download images"

# �� ȭ���� �ش� ��ũ�� ������Ʈ�� ������ �� ���Ǽҵ��� �̹������� �ٿ�ε� �ϴ� �ݺ����Դϴ�
for ep in range(-BEGIN_EPISODE, -LAST_EPISODE - 1, -1):
    print "----------------------------------------"
    print "Trying to request EP", str(-ep) + "'s images..."

    # �ش� ���Ǽҵ� ��ũ�� ������Ʈ�� �����ϴ�
    epResponse = requests.get('http://comics.nate.com' + result[ep]['href'])
    epResponse.raise_for_status()
    print "Got response"

    # �ش� ���Ǽҵ尡 �ִ� �������� �̹������� �Ľ��մϴ�
    imageParser = BeautifulSoup(epResponse.text, "html.parser")
    images = imageParser.select('.toonView > img')

    # ���Ǽҵ� ���� �̹����� ���� ���Ǽҵ� ���丮�� ���� �������ݴϴ�
    # �� ���� ���������� �̹� ���丮�� �ִٸ� ������ ��ϴ�
    epDirPath = os.path.join(newDirPath, 'EP ' + str(-ep))
    os.mkdir(epDirPath)

    # �ش� ���Ǽҵ��� �̹��� ����Ʈ���� �ݺ��Ͽ� �ٿ�ε��մϴ�
    for i in range(0, len(images)):
        print "Downloading images", str(-ep) + "-" + str(i)
        cut = requests.get(images[i]['src'])

        # ����� �̹��� ������ �����մϴ� (ex. '2-1.jpg', '5-2.jpg')
        cutFile = open(os.path.join(epDirPath, str(-ep) + "-" + str(i) + '.jpg'), 'wb')

        for chunk in cut.iter_content(100000):
            cutFile.write(chunk)

        cutFile.close()

print "\nDone"
