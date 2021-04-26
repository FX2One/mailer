import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
import getpass

smtp_server = "smtp.gmail.com"
port = 465  # starttls TransportLayerSecurity

# type in your address
sender_email = input('Type in your email address: ')

# unix like password typing
password = getpass.getpass(prompt='Password: ')

# email subject
subject = input('Type in email subject: ')

# receivers
receiver_email = input('type in receiver: ') #will be changed to read from file

# email message
e_msg = input('Your Message here: ') #will be changed to read from file

#Mime multipart headers
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Bbc'] = receiver_email #blind carbon copy
message['Subject'] = subject


# email body
message.attach(MIMEText(e_msg, "plain"))






# secure SSL certificate
context = ssl.create_default_context()

# create secure connection
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())






