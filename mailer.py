import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
import getpass


smtp_server = "smtp.gmail.com"
port = 465  # starttls TransportLayerSecurity

# type in your address


# unix like password typing
password = getpass.getpass(prompt='Password: ')

# email subject
subject = 'Test email to multiple recipients'

sender_email = 'mskrzypczak2@swps.edu.pl'
to_email = 'mskrzypczak2@swps.edu.pl'
# receivers
receiver_email = 'beleth21@gmail.com'
recipients = ['dfoxik@gmail.com', 'darthfox21@gmail.com']
# email message
#e_msg = 'thats my test message ' # will be changed to read from file

# will be changed for pop-up file dialog box
#fix %username% position
file_location = 'C:\\Users\\mskrzy16\\Downloads\\readme.txt'  # so far takes file from Downloads ,doesn't work quite yet
# stores file_location name of a file we want to attach

# function that gets the last element of a path string to send user only file name not entire path directory
def get_file_name(our_file):
    x = []
    s = our_file.replace('\\',' ')
    for word in s.split():
        x.append(word)
    return x[-1]



#Mime multipart headers
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = to_email
message['Subject'] = subject

f1 = get_file_name(file_location)

# open attachement
attachment = open(file_location, 'rb')
text = input('type in something: ')
# MimeBase instance
part1 = MIMEBase('application', 'octet-stream')
part2 = MIMEText(text, 'plain')
part1.set_payload(attachment.read()) # read the attachment
encoders.encode_base64(part1) # encode to base64
part1.add_header('Content-Disposition', f'attachment; filename= {f1}')
message.attach(part1) # add attachment to message
message.attach(part2)

# secure SSL certificate
context = ssl.create_default_context()

# create secure connection
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, [to_email] + recipients , message.as_string())
    server.quit() # end connection






