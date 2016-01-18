import requests

response = requests.get('https://sdl-stickershop.line.naver.jp/products/0/0/8/718/LINEStorePC/main.png?__=20150924')

try:
    response.raise_for_status()
except Exception as exc:
    print 'There was a problem: %s' % exc

downloadFile = open('myDownFile.png', 'wb')
for chunk in response.iter_content(100000):
    downloadFile.write(chunk)

downloadFile.close()