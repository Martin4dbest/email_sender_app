from email.message import EmailMessage
from config import password
import ssl
import smtplib

email_sender = 'martin4dtruth2@gmail.com'
email_password = password

email_receiver = ['martin4dtruth@gmail.com' , 'pigat77920@jthoven.com', 'msonibe14@gmail.com']

subject = "Message to my brother, Michael"
body = """
This message is coming from Martin through my email sender app. Enjoy your day
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] =subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())