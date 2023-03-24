import smtplib
from email.mime.text import MIMEText

# Email account details
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'your_email_address@gmail.com'
smtp_password = 'your_email_password'

# Email message details
from_email = 'your_email_address@gmail.com'
to_email = 'recipient_email_address@example.com'
subject = 'Test email'
body = 'This is a test email.'

# Create the email message
message = MIMEText(body)
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject

# Connect to the SMTP server and send the email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(from_email, to_email, message.as_string())
