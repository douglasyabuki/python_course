# Sending SMTP Emails with Python
import os
import pathlib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

from dotenv import load_dotenv  # type: ignore

load_dotenv()

# HTML file path
HTML_PATH = pathlib.Path(__file__).parent / 'lesson185.html'

# Sender and receiver details
sender = os.getenv('FROM_EMAIL', '')
recipient = sender  # sending to self (you can change this as needed)

# SMTP Configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# Reading and preparing the HTML message
with open(HTML_PATH, 'r', encoding='utf-8') as file:
    file_text = file.read()
    template = Template(file_text)
    email_text = template.substitute(name='John Doe', me='Joe Tho')

# Creating the email as MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = sender
mime_multipart['to'] = recipient
mime_multipart['subject'] = 'This is the email subject'

email_body = MIMEText(email_text, 'html', 'utf-8')
mime_multipart.attach(email_body)

# Sending the email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('Email sent successfully!')
