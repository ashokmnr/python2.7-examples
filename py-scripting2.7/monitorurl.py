import time
from urllib2 import urlopen
from smtplib import SMTP
from email.mime.text import MIMEText
from datetime import datetime
from datetime import timedelta


def send_alert():
    try:
        msg = MIMEText('Please check the server')
        msg['Subject'] = 'Google is unreachable'
        msg['From'] = 'email'
        msg['To'] = 'email'
        server = SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login('username', 'password')
        server.sendmail('email', [
            'email'], msg.as_string())
        server.quit()
        print ("Done. Sending Email")
    finally:
        print ("Done. Sending Email")


def whileloop(watchtime):
    afterhour = (datetime.now() + timedelta(minutes=watchtime))
    while True:
        after = (datetime.now().strftime("%H-%M"))
        if (after == afterhour.strftime("%H-%M")):
            checkUrl(watchtime)
            break


def checkUrl(watchtime):
    url = 'http://google.com/'
    try:
        urlopen(url)
        print ('OK')
        whileloop(watchtime)
    except:
        send_alert()


checkUrl(1)
