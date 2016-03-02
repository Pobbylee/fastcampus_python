import time
import requests


def print_hello():
    print "Hello, HTML!"
    for cnt in range(5, -1, -1):
        time.sleep(1)
        print cnt


print_hello()

response = requests.get('http://www.naver.com')

try:
    response.raise_for_status()
except Exception as exc:
    print 'There was a problem: %s' % exc

print response.text