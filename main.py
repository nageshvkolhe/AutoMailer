from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import pandas as pd
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get configuration from environment variables
sender_email = os.getenv('SENDER_EMAIL')
app_pass = os.getenv('APP_PASSWORD')
sender_name = os.getenv('SENDER_NAME')
phone_number = os.getenv('PHONE_NUMBER')
email_subject = os.getenv('EMAIL_SUBJECT')
email_body_template = os.getenv('EMAIL_BODY_TEMPLATE')
resume_path = os.getenv('RESUME_PATH')
recruiter_csv_path = os.getenv('RECRUITER_CSV_PATH')
smtp_server = os.getenv('SMTP_SERVER')
smtp_port = int(os.getenv('SMTP_PORT'))

df = pd.read_csv(recruiter_csv_path)
print(df)

for index,row in df.iterrows():
    if row["condition"]==True:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        receiver_email=row["Gmail"]
        msg['To'] = receiver_email
        subject = email_subject
        body = email_body_template.format(
            name=row['Name'],
            phone=phone_number,
            sender_name=sender_name
        )
        msg['Subject'] = subject
        msg.attach(MIMEText(body, "html"))

        filename = resume_path
        with open(filename, "rb") as pdf_file:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(pdf_file.read())

        # Encode file to base64
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f'attachment; filename="{filename}"',
        )
        msg.attach(part)

        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, app_pass)
            server.sendmail(sender_email, receiver_email, msg.as_string())

        print(f"Email sent successfully! to {row['Name']}")
