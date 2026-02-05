import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class NotificationManager:

    def __init__(self):
        self.email = os.environ["MY_EMAIL"]
        self.password = os.environ["MY_EMAIL_PASSWORD"]
        self.smtp_host = os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"]
        self.smtp_port = int(os.environ["EMAIL_PROVIDER_SMTP_PORT"])

    def send_email(self, recipient, body):
        msg = MIMEMultipart()
        msg["From"] = self.email
        msg["To"] = recipient
        msg["Subject"] = "Flight Price Alert"
        msg.attach(MIMEText(body, "plain", "utf-8"))

        with smtplib.SMTP(self.smtp_host, self.smtp_port, timeout=30) as server:
            server.starttls()
            server.login(self.email, self.password)
            server.send_message(msg)
