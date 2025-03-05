# app/utils/email_service.py

import smtplib
from email.mime.text import MIMEText
from app.config import SMTP_USER, SMTP_PASS, SMTP_SERVER, SMTP_PORT

def send_email(to, content, subject):
    msg = MIMEText(content)
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = to

    # Connect using SMTP_SSL and send the email
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(SMTP_USER, to, msg.as_string())


