from email.message import EmailMessage
from config import password
import ssl
import smtplib

email_sender = 'martin4dtruth2@gmail.com'
email_password = password

email_receiver = 'pigat77920@jthoven.com'

subject = "Building an email sender"
body = """
I will walk you through on how to do this
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