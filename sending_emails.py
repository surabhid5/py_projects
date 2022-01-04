import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Surabhi Devgun'
email['to'] = 'surabhid5@gmail.com'
email['subject'] = 'You Won a Million dollars'

#email.set_content('I am a Python Master!')
email.set_content(html.substitute({'name':'TinTin'}),'html')

with smtplib.SMTP(host= 'smtp.gmail.com',port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()#an encription mechanism so we can connect securely to the server
    smtp.login('surabhi.nitj@gmail.com','$ur987397')
    smtp.send_message(email)
    print('all good boss')