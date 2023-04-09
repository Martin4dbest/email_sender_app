# email_sender_app

<h1>EMAIL SENDER WITH PYTHON</h1>
This code sends an email using the Simple Mail Transfer Protocol (SMTP) via a Secure Sockets Layer (SSL) connection. Here is what each line of the code does:

<b>from email.message import EmailMessage</b>: This line imports the EmailMessage class from the email.message module, which we use to create the email message.
<b>from config import password</b>: This line imports the password variable from the config.py file, which is used as the email sender's password.
<b>import ssl</b>: This line imports the Secure Sockets Layer (SSL) module, which we use to create a default SSL context.
<b>import smtplib</b>: This line imports the SMTP module, which we use to create an SMTP object that sends the email.
<b>email_sender = 'martin4dtruth2@gmail.com'</b>: This line sets the email address of the email sender.
<b>email_password = password</b>: This line sets the password of the email sender.
<b>email_receiver</b> = 'pigat77920@jthoven.com': This line sets the email address of the email receiver.
<b>subject = "Building an email sender"</b>: This line sets the subject of the email message.
<b>body = """I will walk you through on how to do this"""</b>: This line sets the body of the email message.
em = EmailMessage(): This line creates a new instance of the EmailMessage class.
em['From'] = email_sender: This line sets the "From" field of the email message.
em['To'] = email_receiver: This line sets the "To" field of the email message.
em['subject'] =subject: This line sets the "Subject" field of the email message.
em.set_content(body): This line sets the body of the email message.
context = ssl.create_default_context(): This line creates a default SSL context.
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:: This line creates an SMTP object that uses SSL to connect to the Gmail SMTP server.
smtp.login(email_sender, email_password): This line logs in to the email account of the sender using their email address and password.
smtp.sendmail(email_sender, email_receiver, em.as_string()): This line sends the email message from the sender's email address to the receiver's email address.
