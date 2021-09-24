import smtplib
import os
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from platform import python_version

server = 'smtp.gmail.com'
user = 'dead.shadow.2707@gmail.com'
password = 'uwmxhrptuspgjuul'


recipient = 'frost-128@mail.ru'
sender = user
subject = 'Confirmation letter'
text = 'If you are reading it call me: <b>8 707 960 93 77</b>'
html = "<html><head></head><body><p>" + text + "</p></body></html>"

filepath = '../email.png'
basename = os.path.basename(filepath)
filesize = os.path.getsize(filepath)

msg = MIMEMultipart('alternative')
msg['Subject'] = subject
msg['From'] = 'Python script <' + sender + '>'
msg['To'] = recipient
msg['Reply-To'] = sender
msg['Return-Path'] = sender
msg['X-Mailer'] = 'Python/' + (python_version())

part_text = MIMEText(text, 'plain')
part_html = MIMEText(html, 'html')
part_file = MIMEBase('application', f'octer-stream; name="{basename}"')
part_file.set_payload(open(filepath, 'rb').read())
part_file.add_header('Content-Description', basename)
part_file.add_header('Content-Description', f'attachment; filename="{basename}"; size={filesize}')
encoders.encode_base64(part_file)

msg.attach(part_text)
msg.attach(part_html)
msg.attach(part_file)

mail = smtplib.SMTP_SSL(server)
mail.login(user, password)
mail.sendmail(sender, recipient, msg.as_string())
print('success')
mail.quit()
