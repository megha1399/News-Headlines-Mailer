from calendar import month
import requests #HTTP Request
from bs4 import BeautifulSoup #Web Scraping
import smtplib #Send mail
from email.mime.multipart import MIMEMultipart #Email Body
from email.mime.text import MIMEText #Email Body
import datetime #System datetime


now = datetime.datetime.now()
content = ''    #Email content

def extract_news(url):
    print("Extracting Hacker News Stories...")
    cnt = ''
    cnt += ('<b>HN Top Stories:</b>\n' + '<br>' + '-'*50 + '<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
        cnt += ((str(i+1) + ":" + tag.text + '\n' + '<br>') if tag.text != 'More' else "")
    return cnt
cnt = extract_news("https://news.ycombinator.com/")
content += cnt
content += "<br>--------<br>"
content += "<br><br>End of Message"

#Prepare to send Email
SERVER = 'smtp.gmail.com'
PORT = 587
TO = '' #List of to address
FROM = '' #From Mail Address
PASS = '' #Password of gmail account(From Address) 

msg = MIMEMultipart()
msg['Subject'] = 'Top News Stories HN [Automated Email]' + ' ' + str(now.day) + ' ' + str(now.month) + str(now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))

print('Initializing Server')
server = smtplib.SMTP(SERVER, PORT)
server.ehlo()
server.set_debuglevel(1)
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent')
server.quit()