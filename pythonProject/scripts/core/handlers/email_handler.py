from fastapi import FastAPI
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from schemas.models import Email
from scripts.constants.email_constants import email_obj
from scripts.core.handlers.book_handler import pipeline_agg

app = FastAPI()


def send_email(email: Email):
    # Set up the email details
    sender_email = email_obj.sender_email
    sender_password = email_obj.sender_password
    receiver_email = email.receiver_email

    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    if email.subject:
        message["Subject"] = email.subject
    else:
        message["Subject"] = "Book borrowing details"
    body = pipeline_agg()
    body = str(body)

    # Add the body to the email
    message.attach(MIMEText(body, "html"))

    try:
        # Create a secure connection to the SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # Login to the sender's email account
        server.login(sender_email, sender_password)

        # Send the email
        server.send_message(message)

        # Close the connection
        server.quit()

        return {"message": "Email sent successfully"}
    except Exception as e:
        return {"message": str(e)}
