import smtplib
# simple mail transfer protocol
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('src/index.html').read_text())
email = EmailMessage()
email['from'] = 'Colin Bazzano'
email['to'] = 'colinbazzano@gmail.com'
email['subject'] = 'Daisy!!!'

email.set_content(html.substitute(name='TinTin'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('colinbazzano96@gmail.com', 'Bazzanos94')
    smtp.send_message(email)
    print('all good!')
