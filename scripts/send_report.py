import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


smtpUser = '' # mail, z którego wysyłasz
smtpPass = '' # hasło

toAdd = '' # mail, na który wysyłasz
fromAdd = smtpUser

subject = 'Przykladowy temat'

msg = MIMEMultipart('alternative')
msg['Subject'] = subject
msg['From'] = fromAdd
msg['To'] = toAdd

text = MIMEText('<img src="cid:image1">', 'html')
msg.attach(text)

image = MIMEImage(open('eloelo.png', 'rb').read())

image.add_header('Content-ID', '<image1>')
msg.attach(image)

s = smtplib.SMTP('smtp.gmail.com', 587)

s.ehlo()
s.starttls()
s.ehlo()

s.login(smtpUser, smtpPass)
s.sendmail(fromAdd, toAdd, msg.as_string())

s.quit()
