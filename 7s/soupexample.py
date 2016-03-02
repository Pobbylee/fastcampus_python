from bs4 import BeautifulSoup

myhtml = open('../160118/hello.html', 'r')
code = myhtml.read()
myhtml.close()

print code

soup = BeautifulSoup(code, 'html.parser')

print soup.select('p')[0]

print soup.select('p')[0].getText()

print soup.select('.circle')

print soup.select('#rect')

print soup.select('html')