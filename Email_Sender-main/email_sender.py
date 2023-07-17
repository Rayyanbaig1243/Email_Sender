# import built in email modules
import smtplib
from email.message import EmailMessage

# Create email instance
email = EmailMessage()

# Give email information
email['from'] = '(Name of Sender)'
email['To'] = '(Recipient Email Address)'
email['Subject'] = '(Subject Line)'
email.set_content("Email Content")

# Make server connection and send
# This configuration is for Gmail Accounts
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('(Insert Email Address Here)', '(Insert Email Password Here)')
    smtp.send_message(email)
    print("Sent Successfully")
