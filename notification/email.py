# language: notification/email.py
from .base import NotificationBase
import smtplib
from email.mime.text import MIMEText

class EmailNotification(NotificationBase):
    def __init__(self, smtp_server, smtp_port, username, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send(self, message):
        msg = MIMEText(message)
        msg['Subject'] = 'Notification'
        msg['From'] = self.username
        msg['To'] = self.username

        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
            server.login(self.username, self.password)
            server.sendmail(self.username, [self.username], msg.as_string())