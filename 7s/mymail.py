import smtplib
from email.mime.text import MIMEText

MY_ID = ''
MY_PASSWORD = ''

msg_from = raw_input("Your name: ")
msg_to = raw_input("His/Her name: ")
msg_subject = raw_input("Subject: ")
msg_body = raw_input("mail content:\n")

msg = MIMEText(msg_body)
msg['From'] = msg_from
msg['To'] = msg_to
msg['Subject'] = msg_subject

mysmtp = smtplib.SMTP('smtp.naver.com', 587)
mysmtp.ehlo()
mysmtp.starttls()
mysmtp.login(MY_ID, MY_PASSWORD)
result = mysmtp.sendmail(MY_ID, [], msg.as_string())
print result
mysmtp.quit()