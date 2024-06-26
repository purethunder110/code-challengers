import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

import os
from dotenv.main import load_dotenv

load_dotenv()

class EmailMessenger:
    def __init__(self):
        self.sender_email = os.getenv("SENDER_MAIL")
        self.sender_password = os.getenv("SENDER_PASSWORD")
        self.smtp_server = os.getenv("SMTP_SERVER")
        self.smtp_port = int(os.getenv("SMTP_PORT"))

    def send_email(self, recipient_email, subject, message, attachments=[]):
        """Sends an email with the specified content and optional attachments.

        Args:
            recipient_email (str): The email address of the recipient.
            subject (str): The subject of the email.
            message (str): The body of the email.
            attachments (list, optional): A list of file paths to attach to the email. Defaults to [].
        """

        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message))

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                if self.smtp_port == 587:
                    server.starttls()  # Enable TLS for non-SSL ports
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, recipient_email, msg.as_string())
            print(f"Email sent successfully to {recipient_email}")
        except Exception as e:
            print(f"Error sending email: {e}")
