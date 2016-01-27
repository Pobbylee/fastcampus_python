import requests
from bs4 import BeautifulSoup
import docx

# crawling
print "Getting list of articles..."
response = requests.get("http://news.naver.com/main/list.nhn?sid1=105&mid=sec&mode=LSD&date=20160127&page=1")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
art_list = soup.select('.type06_headline > li > dl > dt > a')
art_list.extend(soup.select('.type06 > li > dl > dt > a'))

real_list = []
for art in art_list:
    real_list.append(art['href'])

# doc writing
doc = docx.Document()
print "Writing articles to docs..."
for i in set(real_list):
    response = requests.get(i)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.select('#articleTitle')[0].get_text()
    content = soup.select('#articleBodyContents')[0].get_text()

    doc.add_heading(title, 0)
    doc.add_paragraph(content)

    doc.add_page_break()

print "Now saving..."
doc.save('articles.docx')
print "Done"