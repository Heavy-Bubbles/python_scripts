import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import time

smtp_server = ''
smtp_port = ''
smtp_username = ''
smtp_password = ''
app_password = ''

from_email = smtp_username
to_email = ''
subject = 'mushy'
body = 'https://www.youtube.com/watch?v=qk_EYkV2240'

# build email
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body))

# handle attachment
with open('shroomish.gif', 'rb') as f:
    attachment = MIMEApplication(f.read(), _subtype='gif')
    attachment.add_header('Content-Disposition', 'attachment', filename='shroomish.gif')
    msg.attach(attachment)
    
# send email
with smtplib.SMTP_SSL(smtp_server, smtp_port) as smtp:
    smtp.starttls
    smtp.login(smtp_username, app_password)
    for i in range(5):
        smtp.send_message(msg)
        print('mushy sent')
        if i < 4:
            time.sleep(60)
        
    
