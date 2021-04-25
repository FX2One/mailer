import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "smtp.gmail.com"
port = 587  # starttls TransportLayerSecurity
sender_email = input('Type in your email address: ')
password = input("Type your password and press enter: ")
# receivers read from text file
receiver_email = input('type in receiver: ')
# secure SSL certificate
context = ssl.create_default_context()

# create secure connection
with smtplib.SMTP_SSL(smtp_server,port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())






