import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
import getpass


smtp_server = "smtp.gmail.com"
port = 465  # starttls TransportLayerSecurity

# type in your address
sender_email = '' # to be filled later

# unix like password typing
password = getpass.getpass(prompt='Password: ')

# email subject
subject = 'Test email for my stuff'

# receivers
receiver_email = '' # will be changed to read from file

# email message
e_msg = 'thats my test message ' # will be changed to read from file

# will be changed for pop-up file dialog box
#fix %username% position
file_location = 'C:\\Users\\%username%\\Downloads\\readme.txt'  # so far takes file from Downloads ,doesn't work quite yet

# function that gets the last element of a path string to send user only file name not entire path directory
def get_file_name(our_file):
    x = []
    s = our_file.replace('\\',' ')
    for word in s.split():
        x.append(word)
    return x[-1]

# stores file_location name of a file we want to attach
f1 = get_file_name(file_location)

#Mime multipart headers
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Bbc'] = receiver_email #blind carbon copy
message['Subject'] = subject


# open attachement
attachment = open(file_location, 'rb')

# MimeBase instance
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read()) # read the attachment
encoders.encode_base64(part) # encode to base64
part.add_header('Content-Disposition', f'attachment; filename= {f1}')
message.attach(part) # add attachment to message

# secure SSL certificate
context = ssl.create_default_context()

# create secure connection
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()






