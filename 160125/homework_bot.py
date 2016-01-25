
#-*- coding: utf-8 -*-
#포스코 주식의 특정 항목이 특정 조건을 만족할 때 메일을 보내주는 프로그램 (Python27 용)
#POSCO_mailbot_LSH_27.py
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

def sendmemail(eventname, MY_ID, MY_PASSWORD, msg_to):
    msg_from = "Python_bot"
    msg_subject = eventname
    msg_body = eventname

    msg = MIMEText(msg_body)
    msg['From'] = msg_from
    msg['To'] = msg_to
    msg['Subject'] = msg_subject

    mysmtp = smtplib.SMTP('smtp.naver.com', 587)
    mysmtp.ehlo()
    mysmtp.starttls()
    mysmtp.login(MY_ID, MY_PASSWORD)
    result = mysmtp.sendmail(MY_ID, [msg_to], msg.as_string())
    print("mail sent")
    mysmtp.quit()

def checkPOSCO(itemNo, condition, MY_ID, MY_PASSWORD, msg_to):
    theURL = 'http://finance.naver.com/item/sise.nhn?code=005490'
    gook1 = requests.get(theURL)
    soup1 = BeautifulSoup(gook1.text, "html.parser")
    meat = soup1.select('td.num')
    itemNoValue = meat[itemNo].get_text().strip()
    #좌우 공백을 자르고 숫자만 뽑는다.
    itemNoValue = itemNoValue.replace(',','')
    #161,000 을 161000 으로 만든다.
    condition1 = str(itemNoValue) + condition

    if eval(condition1):
        eventname = 'POSCO' + "'s " + str(itemlist[itemNo]) + ': ' + str(itemNoValue) + ' [' + condition + ']'
        print(unicode(eventname))
        sendmemail(eventname, MY_ID, MY_PASSWORD, msg_to)


global itemlist
itemlist = [u'현재가',u'매도호가',u'전일대비',u'매수호가',u'등락률',u'전일가',u'거래량',u'시가',u'거래대금(백만)',u'고가',u'액면가',u'저가',u'상한가',u'전일상한',u'하한가',u'전일하한',u'PER',u'EPS']
print('=' * 70)
print("This bot, using Naver e-mail, will send you a mail \nwhenever your stock(POSCO)'s certain item meets certain condition.")
print('=' * 70)
for k in range(0,len(itemlist)):
    print k,':',itemlist[k],
print("\n\n1/5 Which item?")
itemNo = int(raw_input())
print("\n2/5 In what kind of condition? ex) < 170000")
condition = raw_input()
print("\n3/5 Enter your Naver ID ex) kochujang89")
MY_ID = raw_input() + '@naver.com'
print("\n4/5 Enter your Naver password")
MY_PASSWORD = raw_input()
print("\n5/5 Where do you want to send the mail? ex) sh.cedric.lee@gmail.com")
msg_to = raw_input()
print("\nOK, now working...")
while True:
    checkPOSCO(itemNo, condition, MY_ID, MY_PASSWORD, msg_to)
